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


symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]

class TestCashflowFetch(unittest.TestCase):
	def test_info_history(self):
		for ticker in tickers:
			# always should have info and history for valid symbols
			assert(ticker.info is not None and ticker.info != {})
			assert(ticker.history(period="max").empty is False)
			
	def test_get_cashflow_data(self):
		for ticker in tickers:
			assert(ticker.cashflow.empty is False)

	def test_get_quarterly_cashflow_data(self):
		for ticker in tickers:
			assert(ticker.quarterly_cashflow.empty is False)
  
if __name__ == '__main__':
    unittest.main()
