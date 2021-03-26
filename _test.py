import yfinance as yf
import unittest


symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]

class TestTicker(unittest.TestCase):
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