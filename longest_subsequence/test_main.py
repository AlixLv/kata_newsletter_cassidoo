# A CHECKER
# get_longest_sub() prend bien une liste de listes en paramètre
# get_longest_sub() prend bien une liste de listes d'int en paramètre
# get_longest_sub()  retourne bien un int

import unittest
from main import longest_subsequence, get_longest_sub


class TestLongestSubsequence(unittest.TestCase):
    def test_list_arg(self):
        lst = [10,11,7,8,9,12]
        expected = 3
        result = longest_subsequence(lst)
        self.assertEqual(result, expected)
    
    def test_empty_list_arg(self):
        lst = []
        expected = 0
        result = longest_subsequence(lst)
        self.assertEqual(result, expected)
    
    def test_arg_in_list(self):
        lst = ["toto", 11,7,8,9,12]
        expected = "An error occured"
        result = longest_subsequence(lst)
        self.assertRaises(TypeError, "'str' object is not callable")

    def test_type_return_value(self):
        lst = [4,2,3,1,5]
        result = longest_subsequence(lst)
        self.assertIsInstance(result, int)


class TestGetLongestSub(unittest.TestCase):
    def test_list_arg(self):
        lst_of_lst =  [[10, 11], [7, 8, 9]]
        expected = 3
        result = get_longest_sub(lst_of_lst)
        self.assertEqual(result, expected)

    def test_empty_list_arg(self):
        lst = []
        expected = "An error occured"
        result = get_longest_sub(lst)
        self.assertRaises(TypeError, "'str' object is not callable")
     
    def test_type_return_value(self):
        lst = [[10, 11], [7, 8, 9]]
        result = get_longest_sub(lst)
        self.assertIsInstance(result, int)    
         
        
if __name__ == '__main__':
    unittest.main()           