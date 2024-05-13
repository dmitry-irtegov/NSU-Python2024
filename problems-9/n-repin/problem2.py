import unittest

class TransactionInProgressException(Exception):
    pass

class Storage:
    def __init__(self):
        self.active_transaction = None
        self.storage_dict = {}

    def __getitem__(self, key):
        return self.storage_dict[key]
    
    def edit(self):
        if self.active_transaction is not None:
            raise TransactionInProgressException()
        
        self.active_transaction = Transaction(self)
        return self.active_transaction

class Transaction:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.new_dict = storage.storage_dict.copy()

    def __getitem__(self, key):
        return self.new_dict[key]

    def __setitem__(self, key, value):
        self.new_dict[key] = value

    def __delitem__(self, key):
        del self.new_dict[key]

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.storage.active_transaction = None

        if exc_type is None:
            self.storage.storage_dict = self.new_dict
        else:
            raise exc_value


class StorageTests(unittest.TestCase):
    def test_transaction(self):
        s = Storage()

        with s.edit() as se:
            se['a'] = 15
            se['b'] = 16

        self.assertEqual(s['a'], 15)
        self.assertEqual(s['b'], 16)

    def test_transaction_get(self):
        s = Storage()

        with s.edit() as se:
            se['a'] = 18
            se['b'] = se['a']

        self.assertEqual(s['a'], 18)
        self.assertEqual(s['b'], 18)

    def test_transaction_redefine(self):
        s = Storage()

        with s.edit() as se:
            se['a'] = 15
            se['b'] = 16

        with s.edit() as se:
            se['a'] = 33
            se['b'] = 32

        self.assertEqual(s['a'], 33)
        self.assertEqual(s['b'], 32)

    def test_transaction_delete(self):
        s = Storage()

        with s.edit() as se:
            se['a'] = 15
            se['b'] = 76

        with s.edit() as se:
            del se['a']

        self.assertRaises(KeyError, lambda: s['a'])
        self.assertEqual(s['b'], 76)

    def test_transaction_rollback(self):
        s = Storage()

        with s.edit() as se:
            se['a'] = 1
            se['b'] = 2

        try:
            with s.edit() as se:
                se['a'] = 42
                raise Exception()
                se['b'] = 112
        except Exception:
            ...
        
        self.assertEqual(s['a'], 1)
        self.assertEqual(s['b'], 2)

    def test_transaction_exception(self):
        s = Storage()

        with s.edit() as se:
            se['a'] = 1
            se['b'] = 2

        def throw_exc():
            with s.edit() as se:
                se['a'] = 42
                with s.edit():
                    ...
                se['b'] = 112
        
        self.assertRaises(TransactionInProgressException, throw_exc)


if __name__ == '__main__':
    unittest.main()
