import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import time
import threading
import alpaca_trade_api as tradeapi

# Trading Configuration
symbol = "AAPL"  # Change this to any stock/crypto symbol

# Fetch historical stock data
data = yf.download(symbol, start="2023-01-01", end="2024-01-01")

# Calculate moving averages
data["Short_MA"] = data["Close"].rolling(window=20).mean()  # 20-day MA
data["Long_MA"] = data["Close"].rolling(window=50).mean()  # 50-day MA

# Generate Buy/Sell Signals
data["Buy_Signal"] = data["Short_MA"] > data["Long_MA"]
data["Sell_Signal"] = data["Short_MA"] < data["Long_MA"]

# Define trading decision function
def trading_decision(row):
    if row["Buy_Signal"]:
        return "BUY"
    elif row["Sell_Signal"]:
        return "SELL"
    return "HOLD"

data["Decision"] = data.dropna(inplace=True)  # Remove NaN values from rolling averages

# Plot the stock prices and moving averages
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Stock Price", color="blue")
plt.plot(data["Short_MA"], label="Short MA (20)", color="green")
plt.plot(data["Long_MA"], label="Long MA (50)", color="red")
plt.legend()
plt.title(f"{symbol} Trading Strategy")
plt.show()

# Alpaca API Credentials (Replace with your credentials)
API_KEY = "PKFSGS5CL5D9L3JJ7YUP"
API_SECRET = "jMR4JfDSnjlw37xP6faWU9m3WJzhHR"
BASE_URL = "https://paper-api.alpaca.markets"

# Connect to Alpaca API
try:
    api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)
    account_info = api.get_account()
    print(f"Connected to Alpaca: Account Balance = ${account_info.cash}")
except Exception as e:
    print(f"Error connecting to Alpaca API: {e}")
    exit()

# Risk Management
ENTRY_PRICE = data["Close"].iloc[-1]  # Assume last closing price as entry
STOP_LOSS = ENTRY_PRICE * 0.95  # 5% Stop Loss
TAKE_PROFIT = ENTRY_PRICE * 1.10  # 10% Take Profit

# Track position state
position = None

def execute_trade(symbol, qty, side):
    """Attempts to execute a trade with retry logic."""
    global position
    for _ in range(3):  # Retry 3 times
        try:
            api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type="market",
                time_in_force="gtc"
            )
            print(f"{side.upper()} order placed for {qty} shares of {symbol}.")
            if side == "buy":
                position = "BUY"
            elif side == "sell":
                position = None
            return True  # Successful trade
        except Exception as e:
            print(f"Error executing trade: {e}. Retrying...")
            time.sleep(3)
    print("Trade failed after multiple attempts.")
    return False

def check_trade_signals():
    """Checks live market conditions and executes trades accordingly."""
    global position

    # Fetch real-time price
    try:
        latest_price = yf.Ticker(symbol).history(period="1d", interval="1m")["Close"].dropna().iloc[-1]
    except Exception as e:
        print(f"Error fetching live price: {e}")
        return

    print(f"Live Price: {latest_price}, Entry: {ENTRY_PRICE}, SL: {STOP_LOSS}, TP: {TAKE_PROFIT}")

    # Recalculate moving averages using live price
    updated_close = pd.concat([data["Close"], pd.Series([latest_price])], ignore_index=True)
    short_ma = updated_close.rolling(window=20).mean().iloc[-1]
    long_ma = updated_close.rolling(window=50).mean().iloc[-1]

    if position == "BUY" and latest_price <= STOP_LOSS:
        execute_trade(symbol, 1, "sell")
        print("Stop Loss triggered! Sold position.")

    elif position == "BUY" and latest_price >= TAKE_PROFIT:
        execute_trade(symbol, 1, "sell")
        print("Take Profit reached! Sold position.")

    elif position is None and short_ma > long_ma:
        execute_trade(symbol, 1, "buy")
        print("BUY signal detected! Purchased 1 share.")

def live_price_tracking():
    """Tracks live price updates and checks for trade signals."""
    while True:
        try:
            check_trade_signals()  # Check trade signals
            time.sleep(60)  # Update every minute
        except Exception as e:
            print(f"Error in live tracking loop: {e}")

# Run live tracking in a separate thread
threading.Thread(target=live_price_tracking, daemon=True).start()
