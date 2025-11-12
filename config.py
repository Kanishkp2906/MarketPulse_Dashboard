import os
from dotenv import load_dotenv

load_dotenv()

# Environment variable loaders to get the API keys and variables.
metal_price_api_key = os.getenv('metal_price_api_key')
usd_rate_api_key = os.getenv('usd_rate_api_key')
troy_ounce = os.getenv('troy_ounce')
stocks_data_api_key = os.getenv('stocks_data_api_key')