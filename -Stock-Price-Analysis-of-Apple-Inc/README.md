# Stock Price Analysis of Apple Inc.

Welcome to my first Python Data Analysis Project! 🎉

This project explores the historical stock performance of Apple Inc. using data sourced from both Yahoo Finance and a JSON file provided by IBM Skills Network.The goal is to apply Python skills to clean, analyze, and visualize real-world financial data.

### Project Structure

📦 Stock-Change/
 ┣ 📘 Stock Change.ipynb
 ┣ 📄 README.md
 ┣ 📊 apple.json
 ┗ 📈 Charts 

### Tools & Libraries Used

Python 3
yfinance – for downloading historical stock data
pandas – for data manipulation and analysis
matplotlib & seaborn – for data visualization
urllib.request – for retrieving JSON data
datetime – for working with date ranges

### Key Features of the Analysis

1. Data Retrieval
    Fetched Apple stock data using the yfinance library.
    Downloaded a static Apple stock data file (apple.json) via urllib.
2. Data Wrangling
    Converted date fields to proper datetime format.
    Cleaned missing values and inspected data structure.
    Calculated important metrics like:
    Daily returns
    Moving averages
3. Exploratory Data Analysis (EDA)
    Used descriptive statistics (.describe()) to understand data distribution.
    Created insightful visualizations:
    Line plots of stock prices over time
    Moving average overlays
    Histogram of daily returns
4. Insights
    Observed significant patterns in price movements.
    Evaluated how short-term and long-term trends compare.

### Sample Visualizations

Line Chart of Opening/Closing Prices
20 Day Moving Averages
Histogram of Daily Returns

All charts were generated using matplotlib and provide valuable visual insight into Apple stock's behavior over time.






