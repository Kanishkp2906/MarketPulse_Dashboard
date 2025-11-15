from datetime import datetime
import pymongo
from pymongo.server_api import ServerApi
from config import mongodb_uri
from stocks_data import stocks_data, base_url, api_key

DATE = datetime.now().strftime("%Y%m%d")

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

def mongo_stocks_data():
    
    client = get_db_connection()

    if client:
        db = client['marketpulse_db']
        bse_collection = db['bse_data']
        nse_collection = db['nse_data']
        volume_collection = db['volume_data']

        table_param = {'_id':DATE}

        bse_data = bse_collection.find_one(table_param)
        nse_data = nse_collection.find_one(table_param)

        if bse_data and nse_data:
            return bse_data['bse_list'], nse_data['nse_list']

        else:
            bse_list = stocks_data(base_url, api_key, "BSE")
            nse_list = stocks_data(base_url, api_key, "NSE")

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
                print(f"Error inserting: {e}")

