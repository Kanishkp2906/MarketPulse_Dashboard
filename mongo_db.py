from datetime import datetime
import pymongo
from pymongo.server_api import ServerApi
from config import mongodb_uri
from stocks_data import stocks_data, base_url, api_key
from currencies import getprice
from streamlit import cache_data
import concurrent.futures

DATE = datetime.now().strftime("%Y%m%d")

# Function to establish a connection with the mongo db server.
def get_db_connection():

    try:
        URI = mongodb_uri
        client = pymongo.MongoClient(URI, server_api = ServerApi('1'))

        client.admin.command('ping')
        print('Pinged your deployment. You successfully connected to MongoDB!')
        return client
    
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

@cache_data(ttl='1d')
def mongo_stocks_data():
    
    client = get_db_connection()

    if client:
        db = client['marketpulse_db']
        bse_collection = db['bse_data']
        nse_collection = db['nse_data']

        table_param = {'_id':DATE}

        bse_data = bse_collection.find_one(table_param)
        nse_data = nse_collection.find_one(table_param)

        if bse_data and nse_data:
            return bse_data['bse_list'], nse_data['nse_list']

        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_bse_data = executor.submit(stocks_data, base_url, api_key, "BSE")
                future_nse_data = executor.submit(stocks_data, base_url, api_key, "NSE")

            bse_list = future_bse_data.result()
            nse_list = future_nse_data.result()
            
            if bse_list and nse_list:

                bse_document = {
                    "_id": DATE,
                    "bse_list": bse_list
                }

                nse_document = {
                    "_id": DATE,
                    "nse_list": nse_list
                }

                try:
                    bse_result = bse_collection.insert_one(bse_document)
                    nse_result = nse_collection.insert_one(nse_document)

                    print(f"Successfully inserted BSE document with ID:{bse_result}.")
                    print(f"Successfully inserted NSE document with ID:{nse_result}.")

                    return bse_list, nse_list
                except Exception as e:
                    print(f"Error inserting stocks data: {e}")
                    return None
            else:
                return None
        
    else: 
        return 'Error connecting to Mongo DB.'

@cache_data(ttl='1d')
def mongo_metal_data():

    client = get_db_connection()

    if client:
        db = client['marketpulse_db']
        currency_collection = db["currencies"]

        query_param = {"_id":DATE}

        currencies = currency_collection.find_one(query_param)

        if currencies:
            return currencies['curr_list']
        
        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_metal_prices = executor.submit(getprice.get_metal_price)
                future_usd_rate = executor.submit(getprice.get_usd_rate)
            gold_price, silver_price = future_metal_prices.result()
            usd_rate = future_usd_rate.result()

            currency_doc = {
                "_id": DATE,
                "curr_list": [gold_price, silver_price, usd_rate]
            }

            try:
                currency_result = currency_collection.insert_one(currency_doc)

                print(f"Successfully inserted currencies with ID: {currency_result}")
                return gold_price, silver_price, usd_rate
            except Exception as e:
                print("Error in inserting metal prices:", str(e))
                return None

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_stocks_data = executor.submit(mongo_stocks_data)
    future_metal_data = executor.submit(mongo_metal_data)

db_stocks_data = future_stocks_data.result()
db_metal_data = future_metal_data.result()
