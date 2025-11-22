import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

def get_secret(key):
    
    try:
        if key in st.secrets:
            return st.secrets[key]
    except (FileNotFoundError, AttributeError):
        pass
    
    return os.getenv(key)

# --- Load Variables ---
metal_price_api_key = get_secret('metal_price_api_key')
usd_rate_api_key = get_secret('usd_rate_api_key')
stocks_data_api_key = get_secret('stocks_data_api_key')
troy_ounce = get_secret('troy_ounce')
mongodb_uri = get_secret('mongodb_uri')
