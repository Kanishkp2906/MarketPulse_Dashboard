import requests
import pandas as pd
from config import stocks_data_api_key

api_key = stocks_data_api_key
base_url = "https://indian-stock-exchange-api2.p.rapidapi.com"

# Function to fetch the BSE data.
def bse_data(base_url, api_key):

    bse_url = f"{base_url}/BSE_most_active"
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
    except requests.exceptions.RequestException as e:
            print("Error:", str(e))
            return None

# Function to fetch the NSE data.
def nse_data(base_url, api_key):

    bse_url = f"{base_url}/NSE_most_active"
    headers = {
        "x-rapidapi-key": f"{api_key}",
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }

    try:
        response = requests.get(bse_url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return None

# Function to normalize the json response and return a edited table.
def get_dataframe(table_func):
    dataframe = table_func
    if dataframe:
        dataframe = pd.json_normalize(dataframe)
        dataframe.drop(columns=['bid','ask','low_circuit_limit','up_circuit_limit',
                                    'short_term_trend','long_term_trend','overall_rating'],inplace=True)
        return dataframe
    else:
        return pd.DataFrame()

bse_dataframe = get_dataframe(bse_data(base_url, api_key))
nse_dataframe = get_dataframe(nse_data(base_url, api_key))

# Function to fetch the historical data for a stock.
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
        if response.status_code == 200:
            data = response.json()['datasets'][0]['values']
            if data:
                return data
            else:
                return None
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return None

# Function to make the dataframe of the historical data.
def get_graph_dataframe(symbol):
    graph_data = historical_data(base_url, api_key, symbol)
    if graph_data:
        graph_df = pd.DataFrame(graph_data, columns=['date', 'price'])
        graph_df['date'] = pd.to_datetime(graph_df['date'])
        graph_df['price'] = pd.to_numeric(graph_df['price'])
        graph_df = graph_df.set_index('date')
        return graph_df
    else:
        return pd.DataFrame()

