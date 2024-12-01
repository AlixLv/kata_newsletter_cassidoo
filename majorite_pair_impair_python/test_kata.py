import unittest 
from kata import majority

class TestMainElement(unittest.TestCase):
    def test_one_number(self):
        self.assertEqual(majority([3,1,4,1]), 1)

    def test_odd_numbers(self):
        self.assertTrue(majority([33,44,55,66,77]), "Majority of odd")

    def test_even_numbers(self):
        self.assertTrue(majority([1,2,3,4,4]), "Majority of even")    

    def test_no_majority(self):
        self.assertTrue(majority([1,2,3,4]), "No majority")

