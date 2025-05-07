import unittest
from vertical_scanning import longest_common_prefix

class TestLongestCommonoPrefix(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_num_input(self):
        lst = ["cat", "camera", 2]
        excepted = "Int value are not accepted! You must enter string input"
        result = longest_common_prefix(lst)
        self.assertRaises(TypeError, "object of type 'int' has no len()")

    def test_empty_result(self):
        self.assertEqual(longest_common_prefix(["dog","racecar","car"]), "")
    
    def test_shorter_word_as_prefix(self):
        self.assertEqual(longest_common_prefix(["abc", "abcd", "abcde"]), "abc")    



if __name__ == '__main__':
    unittest.main()          

