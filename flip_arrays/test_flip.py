import unittest
from flip import flip


class TestFlip(unittest.TestCase):
    def setUp(self):
        """Initialisation des données de test"""
        self.test_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    
    def test_horizontal_flip(self):
        """Test inversement en horizontal"""
        expected = [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7]
        ]
        result = flip(self.test_matrix, "horizontal")
        self.assertEqual(result, expected)
        
    def test_vertical_flip(self):
        """Test inversement en vertical"""
        expected = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]
        result = flip(self.test_matrix, "vertical")
        self.assertEqual(result, expected)
    
    def test_empty_matrix(self):
        """Test avec une matrice vide"""
        empty_matrix = []
        result = flip(empty_matrix, "horizontal")
        self.assertEqual(result, [])
        
    def test_non_list_input(self):
        """Test avec des entrées non type liste"""
        direction = "horizontal"
        self.assertEqual(flip("1,2,3", direction), "Input is not a list!")
        self.assertEqual(flip(1234, direction), "Input is not a list!")
    
    def test_invalid_direction(self):
        """Test avec des entrées ne correspondant pas aux directions "vertical" ou "horizontal"""    
        table = [[1,3,2], [5,6,7]]
        self.assertEqual(flip(table, "hello"), "Input is not valid!")
        self.assertEqual(flip(table, "diagonal"), "Input is not valid!")
        
    if __name__ == '__main__':
        unittest.main()   
        
        


        
        


     