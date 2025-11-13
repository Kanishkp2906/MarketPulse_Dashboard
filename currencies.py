import requests
from config import metal_price_api_key, usd_rate_api_key, troy_ounce

class GetPrices:

    def __init__(self):
        self.api_key = metal_price_api_key
        self.base = "INR"
        self.currencies = "XAU,XAG"
        self.base_url = "https://api.metalpriceapi.com/v1/latest?"
    
    # Function to fetch the gold and silver price.
    def get_metal_price(_self):
        url = f"{_self.base_url}api_key={_self.api_key}&base={_self.base}&currencies={_self.currencies}"

        try:
            response = requests.get(url)

            if response.status_code == 200 and response.json()['success'] == True:
                gold_price = (response.json()['rates']["INRXAU"])/float(troy_ounce)
                silver_price = (response.json()['rates']['INRXAG'])/float(troy_ounce)
                return gold_price, silver_price

        except requests.exceptions.RequestException as e:
            print("Error:",str(e))

    # Function to fetch the USD rate.
    @staticmethod
    def get_usd_rate():

        api_key = usd_rate_api_key
        base = "USD"

        url = f'https://anyapi.io/api/v1/exchange/rates?base={base}&apiKey={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status
            usd_rate = response.json()['rates']['INR']
            return usd_rate
        
        except "Error" as e:
            print("Error:", str(e))

getprice = GetPrices()
