# vwap_calculator.py

import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker from start_date to end_date.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_vwap(data):
    """
    Calculate the weekly Volume Weighted Average Price (VWAP) from the stock data.
    """
    # Adding a helper column for 'Price x Volume'
    data['PxV'] = data['Close'] * data['Volume']
    
    # Grouping by week and calculating VWAP
    weekly_data = data.resample('D').sum()
    weekly_data['VWAP'] = weekly_data['PxV'] / weekly_data['Volume']
    
    return weekly_data['VWAP']

def main(tickers):
    """
    Main function to process a list of stock tickers and calculate their weekly VWAP.
    """
    start_date = "2024-01-01"  # Example start date
    end_date = "2024-01-19"    # Example end date
    
    for ticker in tickers:
        print(f"Processing {ticker}...")
        data = fetch_stock_data(ticker, start_date, end_date)
        weekly_vwap = calculate_vwap(data)
        print(f"Weekly VWAP for {ticker}:\n{weekly_vwap}\n")

# Example usage
tickers = ['BND','BRK-B','CVX','EWJ','GLD','GOOGL','OXY','TSLA','VOO','VTI','VXUS','QQQ','TLT']  # Replace with your list of tickers
main(tickers)
