import unittest
from main import findAnagrams


class TestFindAnagrams(unittest.TestCase):
    def test_cas_nominal(self):
        self.assertEqual(findAnagrams("abab", "ab"), [0, 1, 2])

    def test_cas_limite(self):
        self.assertEqual(findAnagrams("fish", "cake"), [])
        
    def test_retour_liste_vide(self):
        self.assertEqual(findAnagrams("fish", ""), [])    

    def test_gestion_erreur(self):
        with self.assertRaises(TypeError):
            findAnagrams(12, "cake")
    
    def test_assert_true(self):
        self.assertTrue(type(findAnagrams("abab", "ab")) is list)    
    
    def test_assert_is_instance(self):
        self.assertIsInstance(findAnagrams("cbaebabacd", "abc"), list)        
            
if __name__ == "__main__":
    unittest.main()   