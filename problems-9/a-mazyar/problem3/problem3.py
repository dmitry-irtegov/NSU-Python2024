from types import FunctionType
import unittest

class Loggable:
    _class_logs = ()

    @staticmethod
    def dont_log(f):
        f._is_logged = False
        return f

    @staticmethod
    def _is_logged(func):
        return (isinstance(func, FunctionType) and 
                func.__name__ != "__init__" and
                getattr(func, '_is_logged', True))

    @staticmethod
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

    def __init__(self):
        self._logs = ()
        # Log object's class and all its base classes
        for clazz in (self.__class__, *self.__class__.__bases__):
            # wrap methods in logged decorator
            if getattr(clazz, 'log_not_started', True):
                for attr in clazz.__dict__.values():
                    if(Loggable._is_logged(attr)):
                        # attribute is a method
                        if attr.__name__[:2] == '__':
                            setattr(clazz, '_' + clazz.__name__ + attr.__name__, Loggable._logged(attr))
                        else:
                            setattr(clazz, attr.__name__, Loggable._logged(attr))
                clazz.log_not_started = False

    def logged_calls(self):
        res = f'{self.__class__.__name__} LOG\n'
        for entry in self._logs:
            res += str(entry) + '\n'
        return res
    
class Parent():
    def speak(self):
        return "Good one"
    
class LoggedIntWrapper(Parent, Loggable):
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
    
    def __private_method(self):
        return "very inner logic"

    @Loggable.dont_log
    def __str__(self):
        return str(self._int)
    
class Child(LoggedIntWrapper):
    log_not_started = True

    def mumble(self):
        return "tata"

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
        except ValueError as _:
            pass
        self.assertEqual(self.logged._logs[0], "Called method \"dec\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[1], "Execution of method \"dec\" concluded with \n\tValueError: Attempted assigning nagative value: -1 to IntWrapper")

        self.logged.inc()
        try:
            self.logged.dec()
        except ValueError as _:
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

    def test_inheritance(self):
        self.logged.speak()
        self.assertEqual(self.logged._logs[0], "Called method \"speak\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[1], "Execution of method \"speak\" concluded with \n\tReturn value: Good one")

        child = Child()
        child.mumble()
        self.assertEqual(child._logs[0], "Called method \"mumble\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(child._logs[1], "Execution of method \"mumble\" concluded with \n\tReturn value: tata")

    def test_private_method(self):
        self.logged._LoggedIntWrapper__private_method()
        self.assertEqual(self.logged._logs[0], "Called method \"__private_method\" with \n\targs: ()\n\tkwargs: {}")
        self.assertEqual(self.logged._logs[1], "Execution of method \"__private_method\" concluded with \n\tReturn value: very inner logic")


    
if __name__ == '__main__':
    unittest.main()