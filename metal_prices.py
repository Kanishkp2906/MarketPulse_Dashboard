import requests
from streamlit import cache_data
from datetime import datetime, timedelta

yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")

class GetPrices:

    def __init__(self):
        self.api_key = "goldapi-18n8vksmhogss74-io"
        self.curr = "INR"
        self.date = yesterday_date
    
    @cache_data
    def get_gold_price(_self):
        symbol = "XAU"
        url = f"https://www.goldapi.io/api/{symbol}/{_self.curr}/{_self.date}"

        headers = {
            "x-access-token": _self.api_key,
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                gold_price = response.json()["price_gram_24k"]
                return gold_price

        except requests.exceptions.RequestException as e:
            print("Error:",str(e))

    @cache_data
    def get_silver_price(_self):
        symbol = "XAG"
        url = f"https://www.goldapi.io/api/{symbol}/{_self.curr}/{_self.date}"

        headers = {
            "x-access-token": _self.api_key,
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                silver_price = response.json()["price_gram_24k"]
                return silver_price

        except requests.exceptions.RequestException as e:
            print("Error:",str(e))

    @staticmethod
    @cache_data
    def get_usd_rate():

        api_key = "rjjrn256usggjs06ko20eojc3t71hghrgek7u1lf0fuoolih4lmqlgo"
        base = "USD"
        symbol = "INR"
        #date = last_week_date

        url = f'https://anyapi.io/api/v1/exchange/rates?base={base}&apiKey={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status
            usd_rate = response.json()['rates']['INR']
            return usd_rate
        
        except "Error" as e:
            print("Error:", str(e))

getprice = GetPrices()

if __name__ == "__main__":
    
    print(getprice.get_gold_price())
    print(getprice.get_silver_price())
    print(getprice.get_usd_rate())