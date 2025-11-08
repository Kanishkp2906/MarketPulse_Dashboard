# Streamlit App: MarketPulse Dashboard

## Overview
MarketPulse Dashboard is a personal project designed to provide real-time insights into Indian stock prices, gold and silver rates, and currency exchange rates. The app is built using Streamlit and integrates multiple APIs and web scraping techniques to fetch and display data interactively.

## Features
- **Dashboard**:
  - Displays gold and silver prices in major Indian cities.
  - Shows USD to INR exchange rates.
- **Stock Prices**:
  - Allows users to select a stock symbol and view its daily OHLCV (Open, High, Low, Close, Volume) data.
  - Fetches stock data dynamically using the Alpha Vantage API.

## Tools and Technologies Used
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and displaying tables.
- **Requests**: For API calls and fetching data from external sources.
- **Web Scraping**: Using `pandas.read_html()` to extract gold, silver, and exchange rate tables from websites.
- **APIs**:
  - [GoldAPI](https://www.goldapi.io/) for fetching gold and silver prices.
  - [Alpha Vantage](https://www.alphavantage.co/) for stock market data.
  - [AnyAPI](https://anyapi.io/) for currency exchange rates.

## Project Structure
- **`main.py`**: Entry point of the application. Handles navigation between the dashboard and stock prices pages.
- **`dashboard.py`**: Contains the logic for displaying gold, silver, and currency exchange rates.
- **`stocks_page.py`**: Handles stock selection and displays stock data.
- **`metal_prices.py`**: Fetches gold, silver, and USD rates using APIs.
- **`stocks_data.py`**: Fetches stock data from Alpha Vantage API and converts it into a Pandas DataFrame.
- **`dashboard_tables.py`**: Scrapes gold, silver, and exchange rate tables from websites.
- **`stocks_tables.py`**: Contains predefined stock symbols for user selection.

## How It Works
1. **Dashboard**:
   - Scrapes gold and silver rates from `goodreturns.in`.
   - Scrapes currency exchange rates from `x-rates.com`.
   - Displays the data in interactive tables using Streamlit.

2. **Stock Prices**:
   - Allows users to select a stock symbol from a predefined list.
   - Fetches daily OHLCV data for the selected stock using the Alpha Vantage API.
   - Displays the data in an interactive table.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kanishkp2906/MarketPulse_Dashboard.git
   cd streamlit-app
   ```
2. Install Dependencies
   ```bash
   pip install -r pyproject.toml
   ```
3. Run the application
   ```bash
   streamlit run main.py
   ```
   