import unittest 

from getSeasonId import get_season_dates

class TestSeasonId(unittest.TestCase):
    
    def test_charlength(self):
        result = get_season_dates()
        result = len(result)
        
        self.assertEqual(result, 7)
        
        
if __name__ == '__main__':
    unittest.main()
