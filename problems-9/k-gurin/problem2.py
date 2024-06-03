import unittest


class Storage:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        raise RuntimeError("Cannot modify data outside of context manager")

    def edit(self):
        return self._StorageEditor(self._data)

    class _StorageEditor:
        def __init__(self, data):
            self._data = data
            self._backup = None

        def __enter__(self):
            self._backup = self._data.copy()
            return self._data

        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is None:
                self._backup.clear()
            else:
                self._data.clear()
                self._data.update(self._backup)


class TestStorage(unittest.TestCase):
    def test_getitem(self):
        s = Storage()
        s._data = {'a': 1, 'b': 2}
        self.assertEqual(s['a'], 1)
        self.assertEqual(s['b'], 2)

    def test_setitem_exception(self):
        s = Storage()
        with self.assertRaises(RuntimeError):
            s['a'] = 1

    def test_edit_context_manager(self):
        s = Storage()
        with s.edit() as se:
            se['a'] = 1
            se['b'] = 2
        self.assertEqual(s['a'], 1)
        self.assertEqual(s['b'], 2)

    def test_edit_context_manager_exception(self):
        s = Storage()
        try:
            with s.edit() as se:
                se['a'] = 1
                raise ValueError("Test exception")
        except ValueError:
            pass
        self.assertNotIn('a', s._data)

    def test_edit_context_manager_data_persistence(self):
        s = Storage()
        s._data = {'a': 1, 'b': 2}
        try:
            with s.edit() as se:
                se['a'] = 10
                raise ValueError("Test exception")
        except ValueError:
            pass
        self.assertEqual(s['a'], 1)
        self.assertEqual(s['b'], 2)


if __name__ == '__main__':
    unittest.main()
