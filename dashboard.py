import streamlit as st
from metal_prices import getprice as gp
from dashboard_tables import gold_table, silver_table, INR_Table
from stocks_page import StocksPage

class Dashboard:

    def __init__(self):
        with st.container():
            self.title = st.title("MarketPulse Dashboard")
            self.subheading = st.text("A quick look to indian stocks and currencies.")
        st.write("")
        st.write("")

        self.gold_price = gp.get_gold_price()
        self.silver_price = gp.get_silver_price()
        self.usd_rate = gp.get_usd_rate()
        self.col1, self.col2, self.col3 = st.columns([1,1,1])

    def gold_price_display(self):

        with self.col1:
            st.write("# 🪙")
            if self.gold_price:
                self.gold_widget = st.metric(label="Gold Price (24k)", value=f"{self.gold_price:.2f} INR")
            else:
                st.error("Failed to fetch gold price.")

    def silver_price_display(self):

        with self.col2:
            st.write("# 🔘")
            if self.silver_price:
                self.silver_widget = st.metric(label='Silver Price (24k)', value=f'{self.silver_price:.2f} INR')
            else:
                st.error("Failed to fetch silver price")

    def usd_rate_display(self):

        with self.col3:
            st.write("# 💲")
            if self.usd_rate:
                self.usd_rate = st.metric(label="USD rate to INR", value=f"{self.usd_rate:.2f} INR")
            else:
                st.error("Failed to fetch USD rate.")

    def metal_city_rates(self):
        st.write("")
        st.write("")

        with st.container():
            st.subheader("Indian Major Cities Gold Rates Today (1 gram)")
            st.dataframe(gold_table)

            st.write("")
            st.write("")

            st.subheader('Indian Major Cities Silver Rates Today')
            st.dataframe(silver_table)

            st.write("")
            st.write("")

            st.subheader("Indian Rupee Exchange Rates Table")
            st.dataframe(INR_Table)
