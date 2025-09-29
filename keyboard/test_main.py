import unittest
from main import min_assembly_time


class TestMinAssemblyTime(unittest.TestCase):
    def test_empty_dict_input(self):
        result = 0
        self.assertEqual(result, min_assembly_time([{}]))
    
    def test_empty_imput(self):
        with self.assertRaises(ValueError):
           min_assembly_time([]) 
    
    def test_unfilled_input(self):
        pass
    
    def test_minimal_input(self):
        result = 2
        self.assertEqual(
            result, 
            min_assembly_time([
                { "name": "keycaps", "arrivalDays": 1, "assemblyHours": 2 }
                ])
            )
    
    def test_wrong_type_input(self):
        with self.assertRaises(TypeError):
            min_assembly_time("test")
    
    def test_wrong_type_arrivalDays(self):
        pass
        
    def test_wrong_type_assemblyHours(self):
        pass
    
    def test_full_input(self):
        pass

    def two_max_days_input(self):
        pass
    
    
    
if __name__ == "__main__":
        unittest.main()