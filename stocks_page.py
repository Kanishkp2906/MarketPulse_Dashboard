import streamlit as st
from stocks_tables import stock_symbols
from database import db_bse_dataframe, db_nse_dataframe
from stocks_data import get_graph_dataframe

class StocksPage:

    def __init__(self):

        self.page_config = st.set_page_config(
            page_title = "Stocks Prices",
            page_icon = "icons/buy.png"
        )
        self.col1, self.col2 = st.columns([0.4,5], vertical_alignment="center")
        with self.col1:
            st.write('')
            st.image("icons/buy.png", width=60)
        with self.col2:
            st.title("Stock Prices")
        self.subheader = st.caption("Top BSE and NSE Stocks just at one glance.")
        self.symbols = stock_symbols

    def stocks_table_display(self):
        st.write("")
        st.write("")

        self.heading = st.markdown("### BSE Most Active Stocks")
        self.bse_table = db_bse_dataframe
        self.bse_table.index = self.bse_table.index 
        st.dataframe(self.bse_table)

        st.write("")
        st.write("")

        self.heading = st.markdown("### NSE Most Active Stocks")
        self.nse_table = db_nse_dataframe
        self.nse_table.index = self.nse_table.index
        st.dataframe(self.nse_table)

        st.write("")
        st.write("")

    def stocks_selectbox(self):
        st.write("")
        st.write("")

        st.markdown("### BSE Stocks last Month Prices")
        self.symbol = st.selectbox("Choose a stock", self.symbols)
        return self.symbol

    def stocks_graph_display(self):
        st.write("")
        st.write("")

        st.markdown(f'### Last Month Prices for {self.symbol}')
        graph_df = get_graph_dataframe(self.symbol)

        if not graph_df.empty:
            st.line_chart(graph_df)
        else:
            st.error("No data available for the selected stock.")

