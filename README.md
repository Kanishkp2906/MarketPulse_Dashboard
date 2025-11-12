# MarketPulse Dashboard

## Overview
MarketPulse Dashboard is a Streamlit-based web application designed to provide real-time insights into Indian stock prices, gold and silver rates, and currency exchange rates. The app integrates multiple APIs and web scraping techniques to fetch and display data interactively.

## Features
### **Dashboard**
- Displays gold and silver prices in major Indian cities.
- Shows USD to INR exchange rates.
- Provides interactive tables for gold, silver, and currency rates.

### **Stock Prices**
- Displays the most active BSE and NSE stocks.
- Allows users to select a stock symbol and view its historical price data.
- Fetches stock data dynamically using APIs.

## Tools and Technologies
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and table generation.
- **Requests**: For API calls to fetch real-time data.
- **Babel**: For formatting currency values.
- **Web Scraping**: Using `pandas.read_html()` to extract gold, silver, and exchange rate tables.
- **SQLite**: For storing fetched data to minimize API calls.

## APIs Used
- **MetalPriceAPI**: For fetching gold and silver prices.
- **AnyAPI**: For currency exchange rates.
- **RapidAPI Indian Stock Exchange API**: For fetching BSE and NSE stock data.

## Project Structure
- **`main.py`**: Entry point of the application. Handles navigation between the dashboard and stock prices pages.
- **`dashboard.py`**: Displays gold, silver, and currency rates along with interactive tables.
- **`stocks_page.py`**: Displays BSE and NSE stock data and historical price graphs.
- **`database.py`**: Handles SQLite database operations for storing and retrieving data.
- **`currencies.py`**: Fetches gold, silver, and USD rates using APIs.
- **`stocks_data.py`**: Fetches stock data and historical price data using APIs.
- **`dashboard_tables.py`**: Scrapes gold, silver, and currency rate tables from websites.
- **`stocks_tables.py`**: Contains predefined stock symbols for user selection.
- **`config.py`**: Loads environment variables for API keys.

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
3. Set ip environment variables
   - Create a .env file in the project directory and add the following:
   ```bash
   metal_price_api_key=<your_metal_price_api_key>
   usd_rate_api_key=<your_usd_rate_api_key>
   stocks_data_api_key=<your_stocks_data_api_key>
   troy_ounce=31.1035
   ```
3. Run the application
   ```bash
   streamlit run main.py
   ```
## How It Works
1. **Dashboard**:
   - Scrapes gold and silver rates from `goodreturns.in`.
   - Scrapes currency exchange rates from `x-rates.com`.
   - Displays the data in interactive tables using Streamlit.

2. **Stock Prices**:
   - Fetches the most active BSE and NSE stocks using RapidAPI.
   - Displays historical price data for selected stocks using line charts.

3. **Database Integration**:
   - Stores fetched data in SQLite to minimize API calls and optimize performance.
   - Fetches stored data for display if available.