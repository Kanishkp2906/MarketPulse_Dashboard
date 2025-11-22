import requests
from streamlit import cache_data
from config import stocks_data_api_key

api_key = stocks_data_api_key
base_url = "https://indian-stock-exchange-api2.p.rapidapi.com"

# Function to fetch the stock data.
@cache_data(ttl='1d')
def stocks_data(base_url, api_key, stock_ex):

    bse_url = f"{base_url}/{stock_ex}_most_active"
    headers = {
        "x-rapidapi-key": f"{api_key}",
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }

    try:
        response = requests.get(bse_url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            if data:
                return data
            else:
                return None
    except requests.exceptions.RequestException as e:
            print("Error:", str(e))
            return None

# Function to fetch the historical data for a stock.
@cache_data(ttl='1d')
def historical_data(base_url, api_key, symbol):
     
    url = f"{base_url}/historical_data"

    querystring = {"stock_name":{symbol},"period":"1m","filter":"price"}

    headers = {
        "x-rapidapi-key": f"{api_key}",
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }
     
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        try:
            volume_data = response.json()['datasets'][3]['values']
            if volume_data:
                return volume_data
        except Exception as e:
            print(f"Error in historical data:", str(e))

    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return None

