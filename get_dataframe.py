import pandas as pd
from stocks_data import historical_data, base_url, api_key
from mongo_db import db_stocks_data

try:
    bse_data, nse_data = db_stocks_data[0], db_stocks_data[1]
except Exception as e:
    print(f"Error occured in mongo_db_data: {e}")
    bse_data, nse_data = None, None

# Function to normalize the json response and return a edited table.
def get_dataframe(stock_data):
    dataframe = stock_data
    if dataframe:
        dataframe = pd.json_normalize(dataframe)
        dataframe.drop(columns=['bid','ask','low_circuit_limit','up_circuit_limit',
                                    'short_term_trend','long_term_trend','overall_rating'],inplace=True)
        dataframe.index = dataframe.index + 1
        return dataframe
    else:
        return pd.DataFrame()

bse_dataframe = get_dataframe(bse_data)
nse_dataframe = get_dataframe(nse_data)

# Function to make the dataframe of the historical data.
def get_graph_dataframe(symbol):
    volume_data = historical_data(base_url, api_key, symbol.lower())
    if volume_data:
        volume_df = pd.DataFrame(volume_data, columns=['date', 'volume', 'delivery'])
        volume_df = volume_df.drop(columns=['delivery'])
        volume_df['date'], volume_df['volume'] = pd.to_datetime(volume_df['date']),pd.to_numeric(volume_df['volume'])

        volume_df = volume_df.set_index('date')
        return volume_df
    else:
        return pd.DataFrame()
