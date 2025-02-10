import unittest
from kata import available_numbers, is_number_available

class TestAvailableNumbers(unittest.TestCase):
    def setUp(self):
        self.unvailable_position = "text"
        self.test_position = "OL"
        self.empty_position = ""
        self.test_lst = [1, 2, 3, 10, 19]
        self.empty_lst = []
        self.test_return = [51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79]  
    
    def test_available_numbers_QB(self):
        expected = [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]
        result = available_numbers("QB", self.test_lst)
        self.assertEqual(result, expected)
        self.assertIsInstance(result, list)
    
    def test_available_number_0L(self):
        result = available_numbers(self.test_position, [50, 55, 60, 65, 70, 75]) 
        self.assertEqual(result, self.test_return)   

    def test_empty_position(self):
        expected = []
        result = available_numbers(self.empty_position, self.test_lst )
        self.assertEqual(result, expected)

    def test_empty_lst(self):
        excepted = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
        result = available_numbers(self.test_position, self.empty_lst)
        self.assertEqual(result, excepted)
        

class TestIsNumberAvailable(unittest.TestCase):
    def test_string_min(self):
        expected = "Error in argument!"
        result = is_number_available("", 10, [1, 2, 3, 10, 19])
        self.assertRaises(TypeError, "'NoneType' object is not callable")
    
    def test_string_max(self):        
        expected = "Error in argument!"
        result = is_number_available(1, "", [1, 2, 3, 10, 19])
        self.assertRaises(TypeError, "'NoneType' object is not callable")   

    def test_empty_lst(self):
        lst = []
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = is_number_available(1, 10, lst)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()          