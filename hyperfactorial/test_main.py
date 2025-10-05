import unittest
from main import hyperfactorial


class TestHyperfactorial(unittest.TestCase):
    def test_int_error_input(self):
        with self.assertRaises(TypeError):
            hyperfactorial("coucou")
    
    def test_negative_error_input(self):
        with self.assertRaises(ValueError):
            hyperfactorial(-2)
    
    def test_zero_output(self):
        self.assertEqual(hyperfactorial(0), 1)
    
    def test_one_output(self):
        self.assertEqual(hyperfactorial(1), 1)
    
    def test_integer_output(self):
        res = 27648
        self.assertIsInstance(res, int)
    
    def test_type_mutiple_outputs(self):
        for n in [0, 1, 2, 3, 4, 5]:
            with self.subTest(n=n):
                res = hyperfactorial(n)
                self.assertIsInstance(res, int)    
    
    def test_increasing_values(self):
        for n in range(1, 6):
            with self.subTest(n=n):
                self.assertLess(hyperfactorial(n), hyperfactorial(n+1))
    
    def test_output(self):
        res = 3319766398771200000
        self.assertEqual(hyperfactorial(7), res)
        
            

if __name__ == '__main__':
    unittest.main()        