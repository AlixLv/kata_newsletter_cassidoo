import unittest 
from kata import evaluate_postfix

class TestEvaluatePostfix((unittest.TestCase)):
    def setUp(self):
        self.test_data = "423+*"
        self.empty_data = ""
        self.minimal_data = "3"
        self.no_operator_data = "43"
        
    def test_result(self):
        expected = '20'
        result = evaluate_postfix(self.test_data)
        self.assertEqual(result, expected)

    def test_empty_result(self):
        result = evaluate_postfix(self.empty_data)
        self.assertIsNone(result)
    
    def test_mini_result(self):
        expected = '3' 
        result = evaluate_postfix(self.minimal_data)
        self.assertEqual(result, expected)   

    def test_mini_result(self):
        expected = '43' 
        result = evaluate_postfix(self.minimal_data)
        self.assertEqual(result, expected)  
    
    def test_type_result(self):
        excepted = '20'
        result = evaluate_postfix(self.test_data) 
        self.assertIsInstance(result, str)   

if __name__ == '__main__':
    unittest.main()          