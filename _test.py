import yfinance as yf


symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]

class TestTicker:
    def test_info_history(self):
        for ticker in tickers:
            # always should have info and history for valid symbols
            assert(ticker.info is not None and ticker.info != {})
            assert(ticker.history(period="max").empty is False)