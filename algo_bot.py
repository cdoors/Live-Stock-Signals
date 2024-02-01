# Creates a BUY/HOLD/SELL signal based on basic mean regression signal
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

def fetch_stock_data(ticker, start_date, end_date=datetime.now().strftime('%Y-%m-%d')):
    """
    Fetch historical stock data for a given ticker from start_date to end_date.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_average_daily_return(stock_data):
    """
    Calculate the average daily return of a stock based on historical data.
    """
    stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
    average_daily_return = stock_data['Daily Return'].mean()
    return average_daily_return

def generate_trading_signal(stock_data, confidence_interval=1):
    """
    Generate a trading signal based on the comparison of the most recent daily return
    and the confidence interval around the average daily return.
    """
    average_daily_return = calculate_average_daily_return(stock_data)
    std_deviation = stock_data['Daily Return'].std()
    
    upper_bound = average_daily_return + (std_deviation * confidence_interval)
    lower_bound = average_daily_return - (std_deviation * confidence_interval)
    most_recent_daily_return = stock_data['Daily Return'].iloc[-1]
    
    if most_recent_daily_return < lower_bound:
        return 'BUY'
    elif most_recent_daily_return > upper_bound:
        return 'SELL'
    else:
        return 'HOLD'

def analyze_tickers(tickers, start_date):
    """
    Analyze a list of tickers and generate trading signals for each.
    """
    signals = {}
    for ticker in tickers:
        stock_data = fetch_stock_data(ticker, start_date)
        trading_signal = generate_trading_signal(stock_data)
        signals[ticker] = trading_signal
    return signals

# Example Usage
tickers = ['BND','BRK-B','CVX','EWJ','GLD','GOOGL','OXY','TSLA','VOO','VTI','VXUS','QQQ','TLT']  # List of stock tickers
start_date = '2010-01-01'

# Analyze tickers and get trading signals
trading_signals = analyze_tickers(tickers, start_date)

print("Trading Signals:")
for ticker, signal in trading_signals.items():
    print(f"{ticker}: {signal}")
