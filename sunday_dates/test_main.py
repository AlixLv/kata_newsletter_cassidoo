import unittest
from main import get_sundays

class TestGetSundays(unittest.TestCase):
    def test_return_list(self):
        year = 2026
        month = 12
        self.assertEqual(get_sundays(year,month), ['2026-12-06', '2026-12-13', '2026-12-20', '2026-12-27'])
    
    def test_minimal_input_year(self):
        year = 1
        month = 12
        self.assertEqual(get_sundays(year, month), ['0001-12-02', '0001-12-09', '0001-12-16', '0001-12-23', '0001-12-30'])
    
    def test_minimal_input_month(self):
        year = 2015
        month = 1
        self.assertEqual(get_sundays(year, month), ['2015-01-04', '2015-01-11', '2015-01-18', '2015-01-25'])
    
    def test_maximal_input_month(self):
        year = 2015
        month = 12
        self.assertEqual(get_sundays(year, month), ['2015-12-06', '2015-12-13', '2015-12-20', '2015-12-27'])
    
    def test_type_input_return(self):
        self.assertIsInstance(get_sundays(2026,8), list)
    
    def test_value_error_year(self):
        with self.assertRaises(ValueError):
            get_sundays(0, 12)
    
    def test_value_error_month(self):
        for month in (0, 13):
            with self.subTest(month=month):
                with self.assertRaises(ValueError):
                    get_sundays(2015, month)


if __name__ == "__main__":
    unittest.main()