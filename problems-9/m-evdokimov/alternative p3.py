import unittest

class MetaLogger(type):
    
    def __new__(cls, name, base, dct):
        
        for clazz in base:
            if clazz.__name__ == 'Logger':
                add_log = clazz._Logger__add_log
            
        for obj_name, obj in dct.items():
            if callable(obj) and not obj_name.startswith('_'):
                dct[obj_name] = cls.__make_method(obj, add_log)
        return super().__new__(cls, name, base, dct)
                
    def __make_method(method, add_log):
        
        def logging_method(self, *args, **kvargs):
            add_log(self, method.__name__)
            method(self, *args, **kvargs)
            
        return logging_method

class Logger(metaclass = MetaLogger):
    
    def __add_log(self, method):
        self.__log.append(method)
        
    def _clear_log(self):
        self.__log.clear()
        
    def _get_log(self):
        return self.__log
    
    def __init__(self):
        self.__log = []
                
class MyClass(Logger):
    
    def __init__(self):
        super().__init__()
        self.some_list = [100, 10, 1]
    
    def method1(self):
        print("m1")

    def method2(self):
        print(self.some_list[1])

    def method3(self, arg1, arg2):
        print("m3", arg1, arg2)
          
class TestLogger(unittest.TestCase):
    
    def setUp(self):
        self.logger = MyClass()
  
    def test_1(self):
        self.logger.method1()
        self.logger.method3('hello', 'world')
        self.logger.method2()
        self.assertEqual(self.logger._get_log(), ['method1', 'method3', 'method2'])
        
    def test_2(self):
        self.logger.method2()
        self.logger.method1()
        self.logger.method3('hello', 'world')
        self.assertEqual(self.logger._get_log(), ['method2', 'method1', 'method3'])
        
    def test_no_method(self):
        with self.assertRaises(AttributeError):
            self.logger.fake_method()
  
if __name__ == "__main__":
    unittest.main()
