import os
import logging
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()
logging.basicConfig(filename="bot.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def get_client():
    return Client(os.getenv("API_KEY"), os.getenv("API_SECRET"), testnet=True)