import requests
from datetime import datetime, timedelta
import pandas as pd
from streamlit import cache_data

api_key = '5T9I2GY1W3LFRPNJ'
base_url = f'https://www.alphavantage.co/query'

@cache_data
def get_stock_data(symbol):
    # Try multiple dates in case the market is closed
    for days_ago in range(1, 4):  # Check the last 3 days
        date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

        stocks_url = f'{base_url}?function=TIME_SERIES_DAILY&symbol={symbol}.BSE&outputsize=compact&apikey={api_key}'
        try:
            response = requests.get(stocks_url)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json().get("Time Series (Daily)", {}).get(date, {})
                if data:
                    return data
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))
            return None
    return None  # Return None if no data is found for the last 3 days

def get_stock_dataframe(symbol):
    stock_data = get_stock_data(symbol)
    if stock_data:
        return pd.json_normalize(stock_data)
    else:
        return pd.DataFrame()  # Return empty DataFrame if no data is available