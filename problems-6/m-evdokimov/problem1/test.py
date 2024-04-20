import unittest
import problem1

test_output = []

def custom_print(*ins, **args):
    word = ins[0] + ins[1]
    test_output.append(word)
    
class Test_mixer(unittest.TestCase):
    
    def setUp(self):
        test_output.clear()
  
    def test_abc(self):
        problem1.mixer("Hello,   world!", 'abc', how_to_print = custom_print)
        self.assertEqual(test_output, ['Hello,', 'wlord!'])
        
    def test_short_words(self):
        problem1.mixer("Hey how are you?", 'random', how_to_print = custom_print)
        self.assertEqual(test_output, ['Hey', 'how', 'are', 'you?'])
        
    def test_very_short_words(self):
        problem1.mixer("Hi, i am an egg!", 'random', how_to_print = custom_print)
        self.assertEqual(test_output, ['Hi,', 'i', 'am', 'an', 'egg!'])
        
    def test_long_string(self):
        problem1.mixer("VeryLongStringThatIHaveToMix", 'abc', how_to_print = custom_print)
        self.assertEqual(test_output, ['VaaeegghHiIiLMnnoorrStTtTvyx'])
        
    def test_exception(self):
        with self.assertRaises(ValueError):
            problem1.mixer("Hello world", 'bobr')
  
if __name__ == "__main__":
  unittest.main()