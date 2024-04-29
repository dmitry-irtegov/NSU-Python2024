import inspect
import unittest

class Reflection:
    
    def __add_log(self, method):
        self.__log.append(method)
        
    def clear_log(self):
        self.__log.clear()
        
    def get_log(self):
        return self.__log
        
    def __getattr__(self, attr):
        self.__add_log(attr)
        for met in self.__subclass_methods:
            if met[0] == attr:
                return met[1]
        raise AttributeError("No Such Attribute Exception: " + attr)
    
    def __init__(self):
        self.__log = []
        self.__subclass_methods = []
        for met in [method for method in inspect.getmembers(type(self), predicate=callable)]:
            if not met[0].startswith('_') and met[0] != 'get_log' and met[0] != 'clear_log':
                self.__subclass_methods.append(met)
                delattr(type(self), met[0])
                
class MyClass(Reflection):
    
    def __init__(self):
        super().__init__()
        self.some_list = [100, 10, 1]
    
    def method1():
        print("m1")

    def method2():
        print("m2")

    def method3(arg):
        print("m3 " + arg)
          
class TestLogger(unittest.TestCase):
    
    logger = MyClass()
    
    def setUp(self):
        self.logger.clear_log()
  
    def test_1(self):
        self.logger.method1()
        self.logger.method3('hello')
        self.logger.method2()
        self.assertEqual(self.logger.get_log(), ['method1', 'method3', 'method2'])
        
    def test_2(self):
        self.logger.method2()
        self.logger.method1()
        self.logger.method3('hello')
        self.assertEqual(self.logger.get_log(), ['method2', 'method1', 'method3'])
        
    def test_no_method(self):
        with self.assertRaises(AttributeError):
            self.logger.fake_method()
  
if __name__ == "__main__":
    unittest.main()