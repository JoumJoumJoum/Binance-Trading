# Trading Bot – Binance Futures Testnet

## Setup
1. Clone the repo
2. Create a virtual environment and activate it
3. pip install -r requirements.txt
4. Create a .env file:
   API_KEY=your_key
   API_SECRET=your_secret

## How to Run

# Market order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# Limit order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000

## Assumptions
- Uses Binance Futures Testnet (USDT-M) only
- API keys must be from testnet.binancefuture.com (Demo version)
- Enable Futures permission must be checked on the API key

## Logs
All API requests, responses and errors are logged to bot.log