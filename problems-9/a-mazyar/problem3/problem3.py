from types import FunctionType
import unittest

def dont_log(f):
    f._is_logged = False
    return f

def _is_logged(func):
    return (isinstance(func, FunctionType) and 
            func.__name__ != "__init__" and
            getattr(func, '_is_logged', True))

def _logged(func):
    def logged_func(self, *args, **kwargs):
        self._logs += (f"Called method \"{func.__name__}\" with \n\targs: {args}\n\tkwargs: {kwargs}", )
        try:
            result = func(self, *args, **kwargs)
        except Exception as e:
            self._logs += (f"Execution of method \"{func.__name__}\" concluded with \n\t{e.__class__.__name__}: {e}", )
            raise e
        
        self._logs += (f"Execution of method \"{func.__name__}\" concluded with \n\tReturn value: {result}", )
        return result
    return logged_func

class Loggable:
    _class_logs = ()

    def __init__(self):
        self._logs = ()
        # wrap methods in logged decorator
        if getattr(self.__class__, 'log_not_started', True):
            for attr in self.__class__.__dict__.values():
                if(_is_logged(attr)):
                    # attribute is a method
                    setattr(self.__class__, attr.__name__, _logged(attr))
            self.__class__.log_not_started = False

    def logged_calls(self):
        res = f'{self.__class__.__name__} LOG\n'
        for entry in self._logs:
            res += str(entry) + '\n'
        return res
    
class LoggedIntWrapper(Loggable):
    def __init__(self):
        super().__init__()
        self._int = 0

    def inc(self):
        self._int += 1
    
    def dec(self):
        if self._int <= 0:
            raise ValueError(f"Attempted assigning nagative value: {self._int - 1} to IntWrapper")
        self._int -= 1

    def add(self, num=1):
        if num==1:
            self.inc()
        else:
            self._int += num
        return self._int

    @dont_log
    def __str__(self):
        return str(self._int)


class LoggingTest(unittest.TestCase):
    def setUp(self):
        self.logged = LoggedIntWrapper()

    def test_no_args(self):
        self.logged.inc()
        self.logged.add()
        self.assertEqual(self.logged._logs[0], "Called method \"inc\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[1], "Execution of method \"inc\" concluded with \n\tReturn value: None")
        self.assertEqual(self.logged._logs[2], "Called method \"add\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[3], "Called method \"inc\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[4], "Execution of method \"inc\" concluded with \n\tReturn value: None")

    def test_args(self):
        self.logged.add(2)
        self.logged.add(2)
        self.assertEqual(self.logged._logs[0], "Called method \"add\" with \n\targs: (2,)\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[1], "Execution of method \"add\" concluded with \n\tReturn value: 2")
        self.assertEqual(self.logged._logs[2], "Called method \"add\" with \n\targs: (2,)\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[3], "Execution of method \"add\" concluded with \n\tReturn value: 4")
    
    def test_exceptions(self):
        try:
            self.logged.dec()
        except ValueError as e:
            pass
        self.assertEqual(self.logged._logs[0], "Called method \"dec\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[1], "Execution of method \"dec\" concluded with \n\tValueError: Attempted assigning nagative value: -1 to IntWrapper")

        self.logged.inc()
        try:
            self.logged.dec()
        except ValueError as e:
            pass
        self.assertEqual(self.logged._logs[2], "Called method \"inc\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[3], "Execution of method \"inc\" concluded with \n\tReturn value: None")
        self.assertEqual(self.logged._logs[4], "Called method \"dec\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[5], "Execution of method \"dec\" concluded with \n\tReturn value: None")

    def test_dont_log(self):
        self.logged.inc()
        self.assertEqual(len(self.logged._logs), 2)

        self.logged.__str__()
        self.assertEqual(len(self.logged._logs), 2)
    

if __name__ == '__main__':
    unittest.main()