import unittest

class MetaLogger(type):
    
    def __new__(cls, name, base, dct):
        
        for clazz in base:
            if clazz.__name__ == 'Logger':
                add_log = clazz._Logger__add_log
                break
            
        for obj_name, obj in dct.items():
            if callable(obj) and not obj_name.startswith('_'):
                print(obj_name)
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

class SuperClass():
    
    def super_method(self):
        print("super_method_call")

class MyClass(Logger, SuperClass):
    
    def __init__(self):
        super().__init__()
        self.some_list = [100, 10, 1]
        
    def __private_method(self):
        return 0
    
    def method_calls_private_method(self):
        print(self.__private_method())
    
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
        
    def test_private_method(self):
        self.logger.method_calls_private_method() # _MyClass__private_method
        self.assertEqual(self.logger._get_log(), ['method_calls_private_method'])
        
    def test_multiple_inheritance(self):
        self.logger.super_method() # Вот тут тяжело 
        self.assertEqual(self.logger._get_log(), [])
        
    def test_no_method(self):
        with self.assertRaises(AttributeError):
            self.logger.fake_method()
  
if __name__ == "__main__":
    unittest.main()

