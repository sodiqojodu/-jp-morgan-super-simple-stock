from typing import List
from enum import Enum
from threading import Lock
from datetime import datetime, timezone
from .exceptions import InvalidPriceError, InvalidDividendError, InvalidTradeError
import logging
#config.configure_logging()
logger = logging.getLogger(__name__)

class StockType(Enum):
    COMMON = 1
    PREFERRED = 2

class Stock:
    def __init__(self, symbol: str, stock_type: StockType, last_dividend: int, fixed_dividend: float, par_value: int):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self._trades = []
        self.lock = Lock()
        


    def dividend_yield(self, price: float) -> float:
        """
        Calculate the dividend yield for a stock based on its type and price.
        """
        if price == 0:
            raise InvalidPriceError("Price cannot be zero")
        if self.stock_type == StockType.COMMON:
            return self.last_dividend / price
        else:  # StockType.PREFERRED
            return (self.fixed_dividend * self.par_value) / price
        
        
    def pe_ratio(self, price: float) -> float:
        """
        Calculate the P/E Ratio for a stock based on the price.
        """
        dividend = self.dividend_yield(price) * price
        if dividend == 0:
            raise InvalidDividendError("Dividend cannot be zero")
        return price / dividend
    
    @property
    def trades(self):
        with self.lock:
            return self._trades.copy()


    def record_trade(self, quantity: int, buy_sell: str, price: float):
        """
        Record a trade for the stock with the provided details.
        """
        if quantity <= 0 or price <= 0:
            raise InvalidTradeError("Quantity and price must be positive values")
        if buy_sell not in ("BUY", "SELL"):
            raise InvalidTradeError("Invalid buy/sell indicator value")
        trade = {
            'timestamp': datetime.now(timezone.utc),
            'quantity': quantity,
            'buy_sell': buy_sell,
            'price': price
        }
        with self.lock:
            self._trades.append(trade)
        logger.info(f"Recorded trade: {trade}")

    def volume_weighted_stock_price(self, time_period: int = 300) -> float:
        """
        Calculate the Volume Weighted Stock Price for the stock based on the trades within the provided time period.
        """
        current_time = datetime.now(timezone.utc)
        with self.lock:
            trades = [trade for trade in self._trades if (current_time - trade['timestamp']).total_seconds() <= time_period]

        if not trades:
            return 0

        total_quantity = sum(trade['quantity'] for trade in trades)
        weighted_sum = sum(trade['price'] * trade['quantity'] for trade in trades)

        return weighted_sum / total_quantity