import sqlite3
from datetime import datetime
from currencies import getprice
import pandas as pd
from stocks_data import bse_dataframe, nse_dataframe

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
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bse_data(
            date DATE,
            ticker STRING,
            company STRING,
            price INT, 
            percent_change INT,
            net_change INT,
            high INT,
            low INT,
            open INT,
            close INT,
            week_52_low INT,
            week_52_high INT,
            PRIMARY KEY (date, ticker)     
        )
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nse_data(
            date DATE,
            ticker STRING,
            company STRING,
            price INT, 
            percent_change INT,
            net_change INT,
            high INT,
            low INT,
            open INT,
            close INT,
            week_52_low INT,
            week_52_high INT,
            PRIMARY KEY (date, ticker)      
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

# Function to insert the stocks dataframe.  
def insert_dataframe(date, dataframe, table_name):
    """Insert a DataFrame into the specified table in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    dataframe = dataframe.rename(columns={
        '52_week_low': 'week_52_low',
        '52_week_high': 'week_52_high'
    })

    # Check if data for the current date already exists
    cursor.execute(f"SELECT * FROM {table_name} WHERE date = ?", (date,))
    existing_data = cursor.fetchone()

    if existing_data:
        print(f"Data for {date} already exists in the {table_name} table. Skipping insertion.")
    else:
        # Iterate through the rows of the DataFrame and insert each row into the table.
        for _, row in dataframe.iterrows():
            cursor.execute(f"""
                INSERT INTO {table_name} (date, ticker, company, price, percent_change, net_change, high, low, open, close, week_52_low, week_52_high)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (date, row['ticker'], row['company'], row['price'], row['percent_change'], row['net_change'],
                  row['high'], row['low'], row['open'], row['close'], row['week_52_low'], row['week_52_high']))
        print(f"Inserted data for {date} into the {table_name} table.")

    conn.commit()
    conn.close()

# Function to fetch the stocks dataframe.
def fetch_dataframe(date, table_name):

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name} WHERE date = ?", (date,))
    rows = cursor.fetchall()
    
    # Get column names from the cursor itself
    columns = [description[0] for description in cursor.description]
    conn.close()

    dataframe = pd.DataFrame(rows, columns=columns)
    
    if 'date' in dataframe.columns:
        dataframe.drop(columns=['date'], inplace=True)
    return dataframe

# Create table by calling the function.
create_tables()
# Get the prices and rates for dashboard.
gold_price, silver_price, usd_rate  = db_prices(DATE)

# Get the stocks dataframe for the stocks page
db_bse_dataframe = fetch_dataframe(DATE, "bse_data")
db_nse_dataframe = fetch_dataframe(DATE, "nse_data")

# If the fetched dataframe is empty then fetch it from the api and insert it.
if db_bse_dataframe.empty and db_nse_dataframe.empty:
    insert_dataframe(DATE, bse_dataframe, "bse_data")
    insert_dataframe(DATE, nse_dataframe, "nse_data")

    db_bse_dataframe = fetch_dataframe(DATE, "bse_data")
    db_nse_dataframe = fetch_dataframe(DATE, "nse_data")


    
