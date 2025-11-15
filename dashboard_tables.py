import pandas as pd
from streamlit import cache_data
from io import StringIO
import requests
from bs4 import BeautifulSoup

# Websites from where dashboard tables are scraped.
gold_table_url = "https://bankbazaar.com/gold-rate-india.html"
silver_table_url = "https://bankbazaar.com/silver-rate-india.html"
exchange_rate_table_url = "https://www.x-rates.com/table/?from=INR&amount=1"

# Fucntion to scrape and return the dataframe of the gold and silver tables.
@cache_data(ttl='1d')
def get_metal_tables(url):

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = BeautifulSoup(response.text, 'lxml')
        tables = [table for table in data.find_all('div', class_='relative w-full overflow-x-auto')]
        dataframe = pd.read_html(StringIO(str(tables[1])))
        if dataframe:
            dataframe[0].index = dataframe[0].index + 1
            return dataframe[0].head(10)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}") 

# Function to scrape the INR exchange rate.
@cache_data(ttl='1d')
def get_exchange_rate_table(url):
    exchange_rate_tables = pd.read_html(url, storage_options={"User-Agent": "Mozilla/5.0"})
    INR_table = exchange_rate_tables[0]
    INR_table.index = INR_table.index + 1
    return INR_table

# Variables for the dashboard.
gold_table = get_metal_tables(gold_table_url)
silver_table = get_metal_tables(silver_table_url)
INR_table = get_exchange_rate_table(exchange_rate_table_url)


