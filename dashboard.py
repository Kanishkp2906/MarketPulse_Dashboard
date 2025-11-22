import streamlit as st
from mongo_db import db_metal_data
from dashboard_tables import gold_table, silver_table, INR_table
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
        self.db_data = db_metal_data

        self.gold_price = self.db_data[0]
        self.silver_price = self.db_data[1]
        self.usd_rate = self.db_data[2]
        self.col1, self.col2, self.col3 = st.columns([1,1,1], vertical_alignment="center")

    # Function to display the gold price.
    def gold_price_display(self):

        with self.col1:
            if self.gold_price:
                st.image("icons/gold.png", width=80)
                formatted_gold_price = format_currency(self.gold_price,"INR",locale="en_IN")
                self.gold_widget = st.metric(label="Gold Price (1gm)", value=formatted_gold_price)
            else:
                st.error("Failed to fetch gold price.")

    # Funtion to display the silver price.
    def silver_price_display(self):

        with self.col2:
            if self.silver_price:
                st.image("icons/silver.png", width=80)
                formatted_silver_price = format_currency(self.silver_price,"INR",locale="en_IN")
                self.silver_widget = st.metric(label='Silver Price (1gm)', value=formatted_silver_price)
            else:
                st.error("Failed to fetch silver price")

    # Function to display the USD rate.
    def usd_rate_display(self):

        with self.col3:
            if self.usd_rate:
                st.image("icons/dollar.png", width=80)
                formatted_usd_rate = format_currency(self.usd_rate,"INR",locale="en_IN")
                self.usd_rate = st.metric(label="USD rate to INR", value=formatted_usd_rate)
            else:
                st.error("Failed to fetch USD rate.")

    # Function to display the tables of the dashboard.
    def metal_city_rates(self):
        st.write("")
        st.write("")

        with st.container():
            st.subheader("Historical Gold Rate in India")
            if not gold_table.empty:
                st.dataframe(gold_table)
            else:
                st.error("Failed to fetch Historical Gold Rate in India.")

            st.write("")
            st.write("")

            st.subheader('Historical Silver Rate in India')
            if not silver_table.empty:
                st.dataframe(silver_table)
            else:
                st.error("Failed to fetch Historical Silver Rate in India.")

            st.write("")
            st.write("")

            st.subheader("Indian Rupee Exchange Rates Table")
            if not INR_table.empty:
                st.dataframe(INR_table)
            else:
                st.error("Failed to fetch Indian Rupee Exchange Rates Table.")
