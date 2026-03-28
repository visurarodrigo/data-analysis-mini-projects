# Apple Stock Analysis (AAPL)

A professional time-series analysis project exploring Apple Inc. stock behavior using Python, Jupyter, and financial market data.

## Overview

This project analyzes historical AAPL data to understand long-term trend, return behavior, and short-term risk patterns.

Core analysis areas:
- price trend and market movement over time
- trading volume behavior
- dividend history exploration
- daily return distribution
- moving averages (20-day and 50-day)
- rolling 20-day volatility

## Repository Structure

```text
-Stock-Price-Analysis-of-Apple-Inc/
  data/
    raw/
      apple.json
      README.md
  notebooks/
    stock_change.ipynb
  reports/
    figures/
      20-Day Rolling Volatility of Apple Stock.png
      Apple Close Price and 20-Day SMA.png
      Apple Close Price with 20-Day and 50-Day Moving Averages.png
      Apple Dividend History Over Time.png
      Apple Stock Closing Price Over Time.png
      Apple Stock Opening Prices Over Time.png
      Apple Stock Trading Volume Over Time.png
      Daily Returns.png
  requirements.txt
  README.md
```

## Tech Stack

- Python
- Jupyter Notebook
- pandas
- matplotlib
- yfinance

## Setup and Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/stock_change.ipynb
```

## Data Sources

- Local metadata file: data/raw/apple.json
- Historical market data: downloaded in-notebook via yfinance

## Outputs

Generated figures are saved in reports/figures and include:
- opening and closing price trends
- trading volume trend
- dividend history
- daily returns histogram
- moving average comparisons
- rolling volatility profile

## Author

Visura Rodrigo
