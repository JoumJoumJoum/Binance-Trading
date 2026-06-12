import logging
from binance.exceptions import BinanceAPIException
from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()
    params = dict(symbol=symbol, side=side, type=order_type, quantity=quantity)
    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Request: {params}")
    try:
        res = client.futures_create_order(**params)
        logging.info(f"Response: {res}")
        return res
    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        raise