import yfinance as yf
import unittest
import urllib

class TestURL(unittest.TestCase):
    # test function to test equality of two value
    def test_base(self):
        base_url = 'https://query1.finance.yahoo.com'
        status_code = urllib.request.urlopen(base_url).getcode()

        # assertEqual() to check equality of first & second value
        self.assertEqual(status_code, 200)
    
    def test_scrape(self):
        scrape_url = 'https://finance.yahoo.com/quote'
        status_code = urllib.request.urlopen(scrape_url).getcode()
        self.assertEqual(status_code, 200)

  
if __name__ == '__main__':
    unittest.main()