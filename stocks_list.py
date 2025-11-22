from get_dataframe import bse_dataframe

def stock_list():
    bse_list = []
    # Appending the company names in the list for the stocks page.
    try:
        for company in bse_dataframe['company']:
            bse_list.append(company)
        return bse_list
    except Exception as e:
        print(f"Error occured in stocks list: {e}")
        return bse_list
