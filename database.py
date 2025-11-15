import sqlite3
from datetime import datetime
from currencies import getprice
import pandas as pd
# from stocks_data import bse_dataframe, nse_dataframe

# Make the database file.
DB_FILE = "marketpulse.db"
# Get today's date.
DATE = datetime.now().strftime("%Y-%m-%d")

# Function to create tables.
def create_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metal_prices(
            date DATE PRIMARY KEY,
            gold_price INT,
            silver_price INT,
            usd_rate INT           
        )
    """)

    conn.commit()
    conn.close()

# Function to fetch the metal prices or to insert them.
def db_prices(date):

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT gold_price, silver_price, usd_rate FROM metal_prices WHERE date = ?", (date,))
    existing_data = cursor.fetchone()
    
    if existing_data:
        conn.commit()
        conn.close()
        return existing_data
    else:
        gold_price, silver_price = getprice.get_metal_price()
        usd_rate = getprice.get_usd_rate()
        cursor.execute("""
            INSERT INTO metal_prices (date, gold_price, silver_price, usd_rate)
            VALUES (?,?,?,?)
        """, (date, gold_price, silver_price, usd_rate))

        conn.commit()
        conn.close()
        return gold_price, silver_price, usd_rate

# Create table by calling the function.
create_tables()
# Get the prices and rates for dashboard.
gold_price, silver_price, usd_rate  = db_prices(DATE)



    
