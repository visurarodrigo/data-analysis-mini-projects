# Raw Data

## File
- `apple.json`

## Description
A single-company metadata snapshot for Apple Inc. used by the stock analysis notebook.
It contains company profile details, market quote fields, financial ratios, and valuation metrics.

## Source
Generated from Yahoo Finance-style company info data (AAPL), exported as JSON.

## Notable Fields
- `symbol`, `shortName`, `longName`
- `currentPrice`, `marketCap`, `currency`
- `totalRevenue`, `netIncomeToCommon`, `freeCashflow`
- `profitMargins`, `operatingMargins`, `returnOnEquity`
- `fiftyTwoWeekHigh`, `fiftyTwoWeekLow`, `averageVolume`

## Usage
Used in `notebooks/stock_change.ipynb` for contextual company and market metadata.
