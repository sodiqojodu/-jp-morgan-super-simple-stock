# test_stock_market.py

import unittest
from stock_market import Stock, StockType, gbce_all_share_index, InvalidPriceError, InvalidDividendError, InvalidTradeError
from datetime import datetime, timezone, timedelta
import time

class TestStockMethods(unittest.TestCase):
    def setUp(self):
        self.common_stock = Stock("TEA", StockType.COMMON, 10, 0, 100)
        self.preferred_stock = Stock("GIN", StockType.PREFERRED, 8, 0.02, 100)

    def test_dividend_yield_common(self):
        self.assertAlmostEqual(self.common_stock.dividend_yield(10), 1)
        self.assertAlmostEqual(self.common_stock.dividend_yield(20), 0.5)

    def test_dividend_yield_preferred(self):
        self.assertAlmostEqual(self.preferred_stock.dividend_yield(50), 0.04)
        self.assertAlmostEqual(self.preferred_stock.dividend_yield(100), 0.02)

    def test_dividend_yield_invalid_input(self):
        with self.assertRaises(InvalidPriceError):
            self.common_stock.dividend_yield(0)

    def test_pe_ratio(self):
        self.assertEqual(self.common_stock.pe_ratio(50), 5)
        self.assertEqual(self.common_stock.pe_ratio(100), 10)
        self.assertEqual(self.preferred_stock.pe_ratio(50), 25)
        self.assertEqual(self.preferred_stock.pe_ratio(100), 50)

    def test_pe_ratio_invalid_input(self):
        with self.assertRaises(InvalidPriceError):
            self.common_stock.pe_ratio(0)
        with self.assertRaises(InvalidDividendError):
            Stock("NO_DIV", StockType.COMMON, 0, 0, 100).pe_ratio(10)

    def test_record_trade(self):
        self.common_stock.record_trade(1, "BUY", 1)
        self.assertEqual(len(self.common_stock.trades), 1)

    def test_record_trade_invalid_input(self):
        with self.assertRaises(InvalidTradeError):
            self.common_stock.record_trade(-1, "BUY", 1)
        with self.assertRaises(InvalidTradeError):
            self.common_stock.record_trade(1, "INVALID", 1)

    def test_volume_weighted_stock_price(self):
        self.common_stock.record_trade(1, "BUY", 1)
        self.common_stock.record_trade(2, "BUY", 2)
        self.assertAlmostEqual(self.common_stock.volume_weighted_stock_price(5), 1.6666666666666667)

    def test_volume_weighted_stock_price_large_time_period(self):
        self.common_stock.record_trade(1, "BUY", 1)
        self.common_stock.record_trade(2, "BUY", 2)
        self.assertEqual(self.common_stock.volume_weighted_stock_price(3600), 1.6666666666666667)

    def test_volume_weighted_stock_price_no_trades(self):
        with self.common_stock.lock:
            self.common_stock._trades = [
                {
                    'timestamp': datetime.now(timezone.utc) - timedelta(seconds=10),
                    'quantity': 1,
                    'buy_sell': 'BUY',
                    'price': 1
                },
                {
                    'timestamp': datetime.now(timezone.utc) - timedelta(seconds=10),
                    'quantity': 2,
                    'buy_sell': 'BUY',
                    'price': 2
                }
            ]
        self.assertEqual(self.common_stock.volume_weighted_stock_price(5), 0)

    def test_volume_weighted_stock_price_large_values(self):
        self.common_stock.record_trade(1000000, "BUY", 1000)
        self.common_stock.record_trade(2000000, "BUY", 2000)
        self.assertAlmostEqual(self.common_stock.volume_weighted_stock_price(5), 1666.6666666666667)

class TestGBCEAllShareIndex(unittest.TestCase):
    def setUp(self):
        self.stocks = [
            Stock("TEA", StockType.COMMON, 0, 0, 100),
            Stock("POP", StockType.COMMON, 8, 0, 100),
            Stock("ALE", StockType.COMMON, 23, 0, 60),
            Stock("GIN", StockType.PREFERRED, 8, 0.02, 100),
            Stock("JOE", StockType.COMMON, 13, 0, 250)
        ]
    
    def test_gbce_all_share_index(self):
        for stock in self.stocks:
            stock.record_trade(1, "BUY", 1)
        self.assertAlmostEqual(gbce_all_share_index(self.stocks, 5), 1.0)

    def test_gbce_all_share_index_invalid_input(self):
        with self.assertRaises(ValueError):
            gbce_all_share_index(self.stocks, 5)

    def test_gbce_all_share_index_large_time_period(self):
        for stock in self.stocks:
            stock.record_trade(1, "BUY", 1)
        self.assertAlmostEqual(gbce_all_share_index(self.stocks, 3600), 1.0)

    def test_gbce_all_share_index_small_time_period(self):
        for stock in self.stocks:
            stock.record_trade(1, "BUY", 1)
        time.sleep(1.1)  # Adding a delay to make the trades older than 1 second
        with self.assertRaises(ValueError):
            gbce_all_share_index(self.stocks, 1)

    def test_gbce_all_share_index_large_values(self):
        for stock in self.stocks:
            stock.record_trade(1000000, "BUY", 1000)
        self.assertAlmostEqual(gbce_all_share_index(self.stocks, 5), 1000.0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

