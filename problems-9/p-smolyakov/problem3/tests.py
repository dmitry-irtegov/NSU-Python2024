from loggable import Loggable

import unittest
import time


class ClassWithLogging(Loggable):
    def sleep_for_sec(self):
        time.sleep(1)


    def no_args(self):
        return 'nanana'


    def multiple_args(self, one, two, three='named', four='args'):
        return three + four


    def do_exception(self):
        raise RuntimeError('Error text')


    def __str__(self):
        return 'Some string'


    def nested_calls(self):
        return str(self)


class LoggableTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._class = ClassWithLogging()
        self._store = self._class.log_storage()


    def test_single_call_no_args(self):
        self._class.no_args()

        self.assertEqual(len(self._store._list), 2)

        self.assertEqual(self._store._list[0].func.__name__, 'no_args')
        self.assertEqual(self._store._list[0].args, (self._class, ))
        self.assertEqual(self._store._list[0].kwargs, {})

        self.assertEqual(self._store._list[1].func.__name__, 'no_args')
        self.assertEqual(self._store._list[1].res, 'nanana')


    def test_single_call_multiple_args(self):
        self._class.multiple_args(1, 2, four = 'GAGAGA')

        self.assertEqual(len(self._store._list), 2)

        self.assertEqual(self._store._list[0].func.__name__, 'multiple_args')
        self.assertEqual(self._store._list[0].args, (self._class, 1, 2))
        self.assertEqual(self._store._list[0].kwargs, {'four': 'GAGAGA'})

        self.assertEqual(self._store._list[0].func.__name__, 'multiple_args')
        self.assertEqual(self._store._list[1].res, 'namedGAGAGA')


    def test_single_call_exception(self):
        exception = None
        try:
            self._class.do_exception()
        except RuntimeError as re:
            exception = re
            pass
        
        self.assertEqual(self._store._list[0].func.__name__, 'do_exception')
        self.assertEqual(self._store._list[1].func.__name__, 'do_exception')
        self.assertEqual(len(self._store._list), 2)
        self.assertEqual(self._store._list[1].exception, exception)


    def test_nested_calls(self):
        self._class.nested_calls()

        self.assertEqual(len(self._store._list), 4)
        self.assertEqual(self._store._list[0].func.__name__, 'nested_calls')
        self.assertEqual(self._store._list[1].func.__name__, '__str__')
        self.assertEqual(self._store._list[2].func.__name__, '__str__')
        self.assertEqual(self._store._list[3].func.__name__, 'nested_calls')


    def test_multi_calls(self):
        self._class.no_args()
        self._class.multiple_args(1, 2)

        self.assertEqual(len(self._store._list), 4)
        self.assertEqual(self._store._list[0].func.__name__, 'no_args')
        self.assertEqual(self._store._list[1].func.__name__, 'no_args')
        self.assertEqual(self._store._list[2].func.__name__, 'multiple_args')
        self.assertEqual(self._store._list[3].func.__name__, 'multiple_args')

    
    def test_multiple_classes(self):
        self._class.no_args()
    
        snd_class = ClassWithLogging()
        snd_class.multiple_args(1, 2)

        self.assertEqual(len(self._store._list), 2)
        self.assertEqual(self._store._list[0].func.__name__, 'no_args')
        self.assertEqual(self._store._list[1].func.__name__, 'no_args')

        self.assertEqual(len(snd_class.log_storage()._list), 2)
        self.assertEqual(snd_class.log_storage()._list[0].func.__name__, 'multiple_args')
        self.assertEqual(snd_class.log_storage()._list[1].func.__name__, 'multiple_args')

    
    def test_timestamp(self):
        self._class.sleep_for_sec()

        self.assertEqual(len(self._store._list), 2)
        start = self._store._list[0].timestamp.timestamp()
        end = self._store._list[1].timestamp.timestamp()
        self.assertTrue(end - start >= 1.0)


if __name__ == '__main__':
    unittest.main()
