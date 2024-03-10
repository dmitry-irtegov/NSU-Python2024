#!/usr/bin/env python3
import unittest

class _ReadOnlyDict:
    def __init__(self):
        self._dict = dict()


    def __getitem__(self, key):
        return self._dict[key]


class _StorageTransaction(_ReadOnlyDict):
    def __init__(self, src_storage):
        _ReadOnlyDict.__init__(self)
        self.__src_storage = src_storage
        self._dict |= src_storage._dict


    def __setitem__(self, key, value):
        self._dict[key] = value


    def __delitem__(self, key):
        try:
            del self._dict[key]
        except KeyError:
            raise KeyError(f'Key {key} doesn\'t exist in current snapshot') from None


    def __enter__(self):
        return self


    def __exit__(self, exception_type, exception_value, traceback):
        self.__src_storage._ongoing_transaction = False
        if exception_type is None:
            self.__src_storage._dict = self._dict
        else:
            raise exception_type(exception_value)
        return True


class Storage(_ReadOnlyDict):
    def __init__(self):
        _ReadOnlyDict.__init__(self)
        self._ongoing_transaction = False


    def edit(self):
        if not self._ongoing_transaction:
            self._ongoing_transaction = True
            return _StorageTransaction(self)
        else:
            raise RuntimeError('some transaction is already in progress')


class StorageTransactionsTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__storage = Storage()


    def test_regular_single_transaction(self):
        with self.__storage.edit() as se:
            se['a'] = 10
            se['b'] = 20
            se[None] = None
            se[True] = False
            se[False] = '0, actually'

        self.assertEqual(self.__storage['a'], 10)
        self.assertEqual(self.__storage['b'], 20)
        self.assertEqual(self.__storage[None], None)
        self.assertEqual(self.__storage[True], False)
        self.assertEqual(self.__storage[False], '0, actually')

        with self.assertRaises(KeyError):
            _ = self.__storage['not exist']
            

    def test_single_transaction_with_redefs(self):
        with self.__storage.edit() as se:
            se['fst'] = 1
            se['snd'] = 2
            se['fst'] = 100500

        self.assertEqual(self.__storage['fst'], 100500)


    def test_single_transaction_deletion(self):
        with self.__storage.edit() as se:
            se[1] = True
            se[2] = True
            del se[1]

        self.assertEqual(self.__storage[2], True)

        with self.assertRaises(KeyError):
            _ = self.__storage[1]


    def test_single_transaction_unsuccessful_deletion(self):
        with self.assertRaises(KeyError):
            with self.__storage.edit() as se:
                se[1] = True
                del se['not exist']


    def test_user_exception(self):
        with self.assertRaises(NotImplementedError):
            with self.__storage.edit() as _:
                raise NotImplementedError            


    def test_nested_transaction_failure(self):
        with self.assertRaises(RuntimeError):
            with self.__storage.edit() as _:
                with self.__storage.edit() as _:
                    pass


    def test_revert_after_exception(self):
        with self.__storage.edit() as se:
            se['one'] = 1

        self.assertEqual(self.__storage['one'], 1)

        try:
            with self.__storage.edit() as se:
                se['one'] = 100500
                se['two'] = 2
                del se['three']
        except KeyError:
            pass

        self.assertEqual(self.__storage['one'], 1)
        with self.assertRaises(KeyError):
            _ = self.__storage['two']
            


    def test_regular_multi_transaction(self):
        with self.__storage.edit() as se:
            se['one'] = 1

        self.assertEqual(self.__storage['one'], 1)
        with self.assertRaises(KeyError):
            _ = self.__storage['two']

        with self.__storage.edit() as se:
            se['two'] = 2

        self.assertEqual(self.__storage['one'], 1)
        self.assertEqual(self.__storage['two'], 2)


    def test_multi_transaction_with_redefs(self):
        with self.__storage.edit() as se:
            se['one'] = 1

        self.assertEqual(self.__storage['one'], 1)

        with self.__storage.edit() as se:
            se['one'] = 2
            
        self.assertEqual(self.__storage['one'], 2)


    def test_multi_transaction_deletion(self):
        with self.__storage.edit() as se:
            se['one'] = 1
            se['two'] = 2

        self.assertEqual(self.__storage['one'], 1)
        self.assertEqual(self.__storage['two'], 2)

        with self.__storage.edit() as se:
            del se['two']

        self.assertEqual(self.__storage['one'], 1)
        with self.assertRaises(KeyError):
            _ = self.__storage['two']


if __name__ == '__main__':
    unittest.main()
