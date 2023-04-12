
import math
from typing import List
from .stock import Stock
from .exceptions import InvalidPriceError

def gbce_all_share_index(stocks: List[Stock], time_period: int = 300) -> float:
    """
    Calculate the GBCE All Share Index for a list of stocks.
    """
    vwsp_list = [stock.volume_weighted_stock_price(time_period) for stock in stocks]
    if not vwsp_list or 0 in vwsp_list:
        raise InvalidPriceError("All stocks must have a non-zero Volume Weighted Stock Price")
    product = math.prod(vwsp_list)
    return math.pow(product, 1 / len(vwsp_list))
