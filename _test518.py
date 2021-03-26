import unittest
import yfinance as yf



symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]

class TestTicker(unittest.TestCase):
    def test_info_history(self):
        for ticker in tickers:
            # always should have info and history for valid symbols
            assert(ticker.info is not None and ticker.info != {})
            assert(ticker.history(period="max").empty is False)

    def test_financials(self):
        for ticker in tickers:
            assert(ticker.financials.empty is False)

    def test_balance_sheet(self):
        for ticker in tickers:
            assert(ticker.balance_sheet.empty is False)
    
    def test_cashflow(self):
        for ticker in tickers:
            assert(ticker.cashflow.empty is False)
    
    def test_quarterlycashflow(self):
        for ticker in tickers:
            assert(ticker.quarterly_cashflow.empty is False)
         
         
            