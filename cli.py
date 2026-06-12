import argparse
from bot.validators import validate
from bot.orders import place_order

parser = argparse.ArgumentParser()
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True, dest="order_type")
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float, default=None)
args = parser.parse_args()

try:
    validate(args.symbol, args.side.upper(), args.order_type.upper(), args.quantity, args.price)
    res = place_order(args.symbol, args.side.upper(), args.order_type.upper(), args.quantity, args.price)
    print(f"Success | ID: {res['orderId']} | Status: {res['status']} | Filled: {res['executedQty']}")
except AssertionError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"Order failed: {e}")