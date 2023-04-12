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

# Testing

The directory tests contains the test suite for the stock market application. The tests cover the main functionality of the application, including the Stock class, stock calculations, and the GBCE All Share Index calculation.

## Test Module Description

- `test_stock_market.py`: Contains unit tests for the Stock class methods, stock calculations, and the GBCE All Share Index calculation.


## Installation

1. Clone the repository:
git clone https://github.com/sodiqojodu/-jp-morgan-super-simple-stock.git

2. Change to the project directory:
cd stock_market

3. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

## Usage

The stock market application is implemented as a Python library. You can import the necessary classes and functions in your Python scripts to work with stocks, trades, and calculations.

Example:

```python
from stock_market import Stock, StockType, gbce_all_share_index

# Create a stock
stock = Stock("TEA", StockType.COMMON, 0, 0, 100)

# Calculate dividend yield
dividend_yield = stock.dividend_yield(50)

# Record a trade
stock.record_trade(1, "BUY", 50)


## Running the Tests 

python -m unittest discover tests
This command will discover and run all tests in the `tests` directory. The test runner will display the results of the tests, including any failures or errors.

## Directory structure
stock_market_app_/
    ├── stock_market/
    │   ├── __init__.py
    │   ├── stock.py
    │   ├── exceptions.py
    │   ├── calculations.py
    │   └── config.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_stock_market.py
    └── README.md