import unittest
from main import odd_sum

class TestOddSum(unittest.TestCase):
    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            odd_sum([],[2, 4, 6, 8])
    
    def test_empty_first_input(self):
        with self.assertRaises(ValueError) as context:
            odd_sum([], [2, 4, 6, 8])
        self.assertEqual(str(context.exception), "Arr1 is empty!")    
    
    def test_empty_second_input(self):
        with self.assertRaises(ValueError) as context:
            odd_sum([2, 4, 6, 8], [])
        self.assertEqual(str(context.exception), "Arr2 is empty!")    
    
    def test_empty_both_inputs(self):
        with self.assertRaises(ValueError) as context:
            odd_sum([], [])
        self.assertEqual(str(context.exception), "Both arrays are empty!")    
    
    def test_minimal_input(self):
        result = [[2, 3], [4, 3], [6, 3], [8, 3]]
        self.assertEqual(result, odd_sum([2, 4, 6, 8], [3]))
        
    def test_type_input(self):
        with self.assertRaises(TypeError) as context:
           odd_sum("test", "test")
        self.assertEqual(str(context.exception), "Both arguments must be of type list!")    
    
    def test_type_return(self):
        message = "Return value is of type list"
        self.assertIsInstance(odd_sum([9, 14, 6, 2, 11], [8, 4, 7, 20]), list, message)