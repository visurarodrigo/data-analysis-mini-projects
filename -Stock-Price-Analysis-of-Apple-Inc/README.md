# Stock Price Analysis of Apple Inc

Time-series exploration project analyzing historical Apple stock behavior using Python.

## Project Overview

This notebook-based project examines Apple stock performance through data retrieval, preparation, and visualization.
The analysis includes:

- historical price and volume trend analysis
- moving average and rolling volatility exploration
- daily return distribution patterns
- dividend history visualization

## Repository Structure

```text
-Stock-Price-Analysis-of-Apple-Inc/
  data/
    raw/
      apple.json
  notebooks/
    stock_change.ipynb
  reports/
    figures/
      20-Day Rolling Volatility of Apple Stock.png
      Apple Close Price & 20-day SMA.png
      Apple Dividend History Over Time.png
      Apple Stock Closing Price Over Time.png
      Apple Stock Opening Prices Over Time.png
      Apple Stock Trading Volume Over Time.png
      Daily Returns.png
  .gitignore
  requirements.txt
  README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/stock_change.ipynb
```

## Data Notes

- The notebook loads JSON data from ../data/raw/apple.json.
- Stock market data is also retrieved via yfinance in the workflow.

## Professional Improvements Applied

- reorganized flat files into standard analytics folders
- moved visual outputs to reports/figures
- standardized notebook naming and path references
- added explicit requirements and repository hygiene rules
- upgraded project documentation for clarity and maintainability

## Author

Visura Rodrigo
