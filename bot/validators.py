def validate(symbol, side, order_type, quantity, price):
    assert symbol.isalnum(), "Invalid symbol"
    assert side in ("BUY", "SELL"), "Side must be BUY or SELL"
    assert order_type in ("MARKET", "LIMIT"), "Type must be MARKET or LIMIT"
    assert quantity > 0, "Quantity must be > 0"
    if order_type == "LIMIT":
        assert price and price > 0, "LIMIT orders require a valid price"