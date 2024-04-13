import unittest
import problem1

test_output = []

def custom_print(*ins, **args):
    word = ins[0]
    test_output.append(word)
    
class Test_mixer(unittest.TestCase):
    
    def setUp(self):
        test_output.clear()
  
    def test_abc(self):
        problem1.mixer("Hello   world !", 'abc', how_to_print = custom_print)
        self.assertEqual(test_output, ['Hello', 'wlord', '!'])
        
    def test_short_words(self):
        problem1.mixer("Hey how are you ?", 'random', how_to_print = custom_print)
        self.assertEqual(test_output, ['Hey', 'how', 'are', 'you', '?'])
        
    def test_exeption(self):
        with self.assertRaises(ValueError):
            problem1.mixer("Hello world", 'bobr')
  
if __name__ == "__main__":
  unittest.main()