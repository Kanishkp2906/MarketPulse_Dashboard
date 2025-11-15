import streamlit as st

# Environment variable loaders to get the API keys and variables.
metal_price_api_key = st.secrets['metal_price_api_key']
usd_rate_api_key = st.secrets['usd_rate_api_key']
troy_ounce = st.secrets['troy_ounce']
stocks_data_api_key = st.secrets['stocks_data_api_key']
mongodb_uri = st.secrets['mongodb_uri']