import unittest 
from main import natoify


class testNatoift(unittest.TestCase):
    def test_input_type(self):
        self.assertIsInstance(natoify("hello world"), str)

    def test_empty_input(self):
        expected = ""
        result = natoify("")
        self.assertEqual(result, expected)
    
    def test_mini_letter_input(self):
        expected = "Alfa"
        result = natoify("a")
        self.assertEqual(result, expected)
     
    def test_mini_num_input(self):
        excepted = "Three"
        result = natoify("3")
        self.assertEqual(result, excepted)
    
    def test_output_value(self):
        expected = "Hotel Echo Lima Lima Oscar (space) Whiskey Oscar Romeo Lima Delta"
        result = natoify("hello world")
        self.assertEqual(result, expected)
    
    def test_output_type(self):
        expected = "Three Sierra Papa Oscar Oscar Kilo Yankee Five Mike Echo"
        result = natoify('3spooky5me')
        self.assertIsInstance(result, str)
        
        
if __name__ == '__main__':
    unittest.main()       