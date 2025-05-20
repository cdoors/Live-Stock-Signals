# Live-Stock-Signals
Exploring basic quantitative trading signals on stock data scraped Yahoo Finance

This repository provides a simple Python that generates **BUY**, **HOLD**, or **SELL** signals based on recent market overreactions relative to historical average returns. It applies a basic **mean reversion strategy** using Yahoo Finance data.

## Overview

This tool evaluates the most recent daily return of a given stock and compares it to a confidence interval (based on standard deviation) around its average historical return. It helps identify short-term **overbought or oversold** conditions that might revert to the mean.

### Signal Logic:

* **BUY**: Most recent return < average - (std × confidence interval)
* **SELL**: Most recent return > average + (std × confidence interval)
* **HOLD**: Otherwise

## Example Output

```
Trading Signals:
BND: HOLD
BRK-B: BUY
CVX: SELL
...
```

## How It Works

```python
tickers = ['BND','BRK-B','CVX',...]  # List of tickers
start_date = '2010-01-01'

trading_signals = analyze_tickers(tickers, start_date)
```

### Core Functions:

* `fetch_stock_data(ticker, start_date)`: Pulls historical price data from Yahoo Finance.
* `calculate_average_daily_return(stock_data)`: Computes mean daily returns.
* `generate_trading_signal(stock_data, confidence_interval=1)`: Determines the BUY/HOLD/SELL signal.
* `analyze_tickers(ticker_list, start_date)`: Runs the analysis for a list of tickers.

## Requirements

Install dependencies using:

```bash
pip install yfinance pandas numpy
```
## License

MIT License

## Disclaimer: Don't Trade on This! Research/Proof of Concept Only


