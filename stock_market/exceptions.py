# exceptions.py

class InvalidPriceError(ValueError):
    """Exception raised when an invalid price is provided."""
    pass


class InvalidDividendError(ValueError):
    """Exception raised when an invalid dividend value is encountered."""
    pass


class InvalidTradeError(ValueError):
    """Exception raised when an invalid trade is attempted."""
    pass
