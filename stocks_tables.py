# import pandas as pd
# from streamlit import cache_data


# gainers_table_url = "https://www.nseindia.com/market-data/top-gainers-losers#gainers"

# def gainers_table(url):
#     table = pd.read_html(url, storage_options={"User-Agent": "Mozilla/5.0"})
#     gainers_df = pd.DataFrame(table).reset_index(drop=True)
#     return gainers_df

# print(gainers_table(gainers_table_url))

stock_symbols = [
    None,
    "RELIANCE",
    'TCS',
    'HDFCBANK',
    'INFY',
    'HINDUNILVR',
    'HDFC',
    'ICICIBANK',
    'KOTAKBANK',
    'SBIN',
    'BAJFINANCE',
]