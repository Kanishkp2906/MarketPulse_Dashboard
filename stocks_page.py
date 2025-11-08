import streamlit as st
from stocks_tables import stock_symbols
from stocks_data import get_stock_dataframe

class StocksPage:

    def __init__(self):
        self.title = st.title("Stock Prices")
        self.subheader = st.text("Daily Gaining and Losing stock prices just at one glance.")
        self.symbols = stock_symbols

    def stocks(self):
        st.write("")
        st.write("")

        st.markdown("### Top Ten BSE Stocks OHLCV")
        # Set self.symbol as the selected stock
        self.symbol = st.selectbox("Choose a stock", self.symbols)

    def stocks_data_display(self):
        st.write("")
        st.write("")

        st.markdown(f'### Stock Data for {self.symbol}')
        stock_df = get_stock_dataframe(self.symbol)

        if not stock_df.empty:
            st.dataframe(stock_df)
        else:
            st.error("No data available for the selected stock.")