import unittest
from main import is_valid_traffic_sequence


class TestIsValidTrafficSequence(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(is_valid_traffic_sequence([]), False)
    
    def test_minimal_inputs(self):
        minimal_inputs = [
            ["green"],
            ["green", "red"]
        ]
        for input in minimal_inputs:
            self.assertEqual(is_valid_traffic_sequence(input), False)
    
    def test_valid_input(self):
        self.assertEqual(is_valid_traffic_sequence(
            ["red", "green", "yellow", "red", "green", "yellow"]
            ), True)
    
    def test_uppercase_input(self):
        self.assertTrue(is_valid_traffic_sequence(
           ["Red", "Green", "Yellow"] 
        ), True)
    
    def test_wrong_type_input(self):
        with self.assertRaises(TypeError):
            is_valid_traffic_sequence("Yellow, Green, Red")
    
    def test_wrong_type_element_in_input(self):
        with self.assertRaises(TypeError):
            is_valid_traffic_sequence(["Red", "Green", 12])
    
    
    def test_assert_return_isinstance_bool(self):
        self.assertIsInstance(is_valid_traffic_sequence(
            ["Red", "Green", "Yellow"]
            ), bool)



if __name__ == '__main__':
    unittest.main()         