# Stock Market Application

This is the Global Beverage Corporation Exchange stock market trading application that allows users to manage stocks, record trades, and calculate stock-related metrics such as dividend yield, P/E ratio, and the GBCE All Share Index.

## Features

- Manage stocks and their properties such as symbol, type, last dividend, fixed dividend, and par value.
- Record trades for stocks, including quantity, buy/sell indicator, and price.
- Calculate stock metrics like dividend yield and P/E ratio based on the stock price.
- Compute the Volume Weighted Stock Price for stocks based on trades within a specific time period.
- Calculate the GBCE All Share Index for a list of stocks.

## Module Descriptions

- `calculations.py`: Contains functions for the GBCE All Share Index.
- `config.py`: Configuration module for setting up logging.
- `exceptions.py`: Custom exceptions for error handling in the application.
- `stock.py`: Defines the Stock class for managing stocks and their trades, along with related methods for calculations like dividend yield, P/E ratio


## Installation

 cd stock_market


1. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate



## Usage

# The stock market application is implemented as a Python library. You can import the necessary classes and functions in your Python scripts to work with stocks, trades, and calculations.

Example:

```python
from stock_market import Stock, StockType, gbce_all_share_index

# Create a stock
stock = Stock("TEA", StockType.COMMON, 0, 0, 100)

# Calculate dividend yield
dividend_yield = stock.dividend_yield(50)

# Record a trade
stock.record_trade(1, "BUY", 50)

## Testing
#To run the test suite, execute the following command in the project directory:

python -m unittest discover tests
