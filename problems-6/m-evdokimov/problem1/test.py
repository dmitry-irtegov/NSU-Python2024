import unittest
import problem1
    
class Test_mixer(unittest.TestCase):
        
    def custom_print(self, *ins, **args):
        self.test_output = ''.join(ins)
    
    def setUp(self):
         self.test_output = ""
  
    def test_abc(self):
        problem1.mixer("Hello,   world!", 'abc', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, 'Hello,   wlord!')
        
    def test_punctuations_abc(self):
        problem1.mixer("((Hello,)  world!)", 'abc', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, '((Hello,)  wlord!)')
        
    def test_punctuations_random(self):
        problem1.mixer("..,Hi,.,.,. ????all!", 'abc', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, '..,Hi,.,.,. ????all!')
        
    def test_short_words(self):
        problem1.mixer("Hey how are you?", 'random', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, 'Hey how are you?')
        
    def test_very_short_words(self):
        problem1.mixer("Hi, i am an egg!", 'random', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, 'Hi, i am an egg!')
        
    def test_long_string(self):
        problem1.mixer("VeryLongStringThatIHaveToMix", 'abc', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, 'VaaeegghHiIiLMnnoorrStTtTvyx')
        
    def test_with_hypen(self):
        problem1.mixer("Some-thing", 'abc', how_to_print = self.custom_print)
        self.assertEqual(self.test_output, 'Smoe-thing')
        
    def test_exception(self):
        with self.assertRaises(ValueError):
            problem1.mixer("Hello world", 'bobr')
  
if __name__ == "__main__":
  unittest.main()