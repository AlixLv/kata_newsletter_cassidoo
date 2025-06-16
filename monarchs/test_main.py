import unittest
from main import sort_monarchs


class TestSortMonarchs(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sort_monarchs([]), [])
    
    def test_large_input(self):
        self.assertEqual(sort_monarchs(
            ["George VI", "Elizabeth I", "George V", "Elizabeth II", "George IV", "Edward VIII"]
            ), 
            ['Edward VIII', 'Elizabeth I', 'Elizabeth II', 'George IV', 'George V', 'George VI']             
            )
    
    def test_minimal_input(self):
        self.assertEqual(sort_monarchs(["Louis IX"]), ["Louis IX"])
    
    def test_type_input(self):
        with self.assertRaises(TypeError):
            sort_monarchs("Louis IX")
    
    def test_type_element_in_input(self):
        with self.assertRaises(TypeError):
            sort_monarchs(["Louis IX", "Philip II", "Philip I", 23])

    def test_type_return(self):
        self.assertIsInstance(sort_monarchs(["Louis IX", "Louis VIII", "Philip II", "Philip I"]), list)
    

if __name__ == "__main__":
    unittest.main()    