import pandas as pd
import numpy as np
import yfinance as yf
import alpaca_trade_api as tradeapi
import time
import schedule
from ta.trend import EMAIndicator
from datetime import datetime

# Step 1: Setup API Credentials
API_KEY = "PKHBOWE5ICZZ6ARJ7CY8"
API_SECRET = "p2ml1GgfKFYXreW7UoQX80MmCz8JMaIpi0cbqRWy"
BASE_URL = "https://paper-api.alpaca.markets"  # Paper trading for testing

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

# Step 2: Get Stock Data (SPX & SPY)
def get_stock_data(ticker):
    """
    Fetches stock data and calculates EMAs.
    """
    df = yf.download(ticker, period="7d", interval="5m")  # 5-min data for 7 days
    df["EMA_9"] = EMAIndicator(close=df["Close"], window=9).ema_indicator()  # 9-period EMA
    df["EMA_21"] = EMAIndicator(close=df["Close"], window=21).ema_indicator()  # 21-period EMA
    return df

# Step 3: Define Trading Strategy (EMA Crossover)
def trading_strategy():
    """
    Checks for EMA crossovers and executes short trades.
    """
    tickers = ["SPY", "SPX"]
    for ticker in tickers:
        df = get_stock_data(ticker)

        # Get last and previous row for EMA crossover
        last_row = df.iloc[-1]
        prev_row = df.iloc[-2]

        # Bearish crossover: Short when EMA 9 crosses below EMA 21
        if prev_row["EMA_9"] > prev_row["EMA_21"] and last_row["EMA_9"] < last_row["EMA_21"]:
            print(f"🔻 Bearish crossover detected on {ticker} - Shorting!")
            execute_trade(ticker, "sell", qty=1)
        else:
            print(f"📊 No trade signal for {ticker} at {datetime.now()}")

# Step 4: Execute Trades
def execute_trade(ticker, side, qty=1):
    """
    Places a market order via Alpaca API.
    """
    try:
        order = api.submit_order(
            symbol=ticker,
            qty=qty,
            side=side,  # "sell" for shorting
            type="market",
            time_in_force="day"
        )
        print(f"✅ Trade executed: {side.upper()} {qty} shares of {ticker}")
    except Exception as e:
        print(f"⚠️ Trade failed: {e}")

# Step 5: Run the Bot (Every 15 Minutes)
schedule.every(15).minutes.do(trading_strategy)

print("🚀 Trading bot is running... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
