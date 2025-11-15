from get_dataframe import bse_dataframe

bse_list = []

# Appending the company names in the list for the stocks page.
for company in bse_dataframe['company']:
    bse_list.append(company)


