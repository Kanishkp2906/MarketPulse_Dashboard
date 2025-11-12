import pandas as pd
from streamlit import cache_data

# Websites from where dashboard tables are scraped.
gold_table_url = "https://www.goodreturns.in/gold-rates/"
silver_table_url = "https://www.goodreturns.in/silver-rates/"
exchange_rate_table_url = "https://www.x-rates.com/table/?from=INR&amount=1"

# Function to scrape the gold table.
@cache_data
def get_gold_table(url):
    gold_tables = pd.read_html(url, storage_options={'User-Agent': 'Mozilla/5.0'})
    gold_table = gold_tables[3]
    gold_table.index = gold_table.index + 1
    return gold_table

# Function to scrape the silver table.
@cache_data
def get_silver_table(url):
    silver_tables = pd.read_html(url, storage_options={"User-Agent": "Mozilla/5.0"})
    silver_table = silver_tables[1]
    silver_table.index = silver_table.index + 1
    return silver_table

# Function to scrape the INR exchange rate.
@cache_data
def get_exchange_rate_table(url):
    exchange_rate_tables = pd.read_html(url, storage_options={"User-Agent": "Mozilla/5.0"})
    INR_table = exchange_rate_tables[0]
    INR_table.index = INR_table.index + 1
    return INR_table

# Variables for the dashboard.
gold_table = get_gold_table(gold_table_url)
silver_table = get_silver_table(silver_table_url)
INR_Table = get_exchange_rate_table(exchange_rate_table_url)
