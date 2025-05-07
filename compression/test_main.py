import unittest

from main import compress


class TestCompress(unittest.TestCase):
    def test_empty_input(self):
        empty_list = []
        expected = []
        result = compress(empty_list)
        self.assertEqual(expected, result)


    def test_minimal_input(self):
        mini_input = ["a"]
        expected = ["a"]
        result = compress(mini_input)
        self.assertEqual(expected, result)

    def test_type_return(self):
        input = ["a", "a", "b", "b", "c", "c", "c"]
        result = compress(input)
        self.assertIsInstance(result, list)

    def test_type_error_input(self):
        error_input = ["a", "a", 3, "b", "c", "c"]
        result = compress(error_input)
        self.assertRaises(TypeError)
    
if __name__ == "__main__":
    unittest.main()        
        