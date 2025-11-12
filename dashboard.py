import streamlit as st
from database import gold_price, silver_price, usd_rate
from dashboard_tables import gold_table, silver_table, INR_Table
from babel.numbers import format_currency

class Dashboard:

    def __init__(self):
        self.page_config = st.set_page_config(
            page_title = "Dashboard",
            page_icon = "icons/dashboard.png"
        )
        self.col1, self.col2 = st.columns([0.4,5], vertical_alignment="center")
        with self.col1:
            st.write('')
            st.image("icons/dashboard.png", width=40)
        with self.col2:
            self.title = st.title("MarketPulse Dashboard")
        self.subheading = st.caption("A quick look to indian stocks and currencies.")
        st.write("")
        st.write("")

        self.gold_price = gold_price
        self.silver_price = silver_price
        self.usd_rate = usd_rate
        self.col1, self.col2, self.col3 = st.columns([1,1,1])

    # Function to display the gold price.
    def gold_price_display(self):

        with self.col1:
            st.image("icons/gold.png", width=80)
            if self.gold_price:
                formatted_gold_price = format_currency(self.gold_price,"INR",locale="en_IN")
                self.gold_widget = st.metric(label="Gold Price (1gm)", value=formatted_gold_price)
            else:
                st.error("Failed to fetch gold price.")

    # Funtion to display the silver price.
    def silver_price_display(self):

        with self.col2:
            st.image("icons/silver.png", width=80)
            if self.silver_price:
                formatted_silver_price = format_currency(self.silver_price,"INR",locale="en_IN")
                self.silver_widget = st.metric(label='Silver Price (1gm)', value=formatted_silver_price)
            else:
                st.error("Failed to fetch silver price")

    # Function to display the USD rate.
    def usd_rate_display(self):

        with self.col3:
            st.image("icons/dollar.png", width=80)
            if self.usd_rate:
                formatted_usd_rate = format_currency(self.usd_rate,"INR",locale="en_IN")
                self.usd_rate = st.metric(label="USD rate to INR", value=formatted_usd_rate)
            else:
                st.error("Failed to fetch USD rate.")

    # Function to display the tables of the dashboard.
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

