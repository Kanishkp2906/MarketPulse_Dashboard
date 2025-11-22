import streamlit as st
from stocks_list import stock_list
from get_dataframe import bse_dataframe, nse_dataframe, get_graph_dataframe

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
        self.symbols = stock_list()

    # Function to display the stocks table.
    def stocks_table_display(self):
        st.write("")
        st.write("")

        self.heading = st.markdown("### BSE Most Active Stocks")
        self.bse_table = bse_dataframe
        self.bse_table.index = self.bse_table.index + 1
        st.dataframe(self.bse_table)

        st.write("")
        st.write("")

        self.heading = st.markdown("### NSE Most Active Stocks")
        self.nse_table = nse_dataframe
        self.nse_table.index = self.nse_table.index + 1
        st.dataframe(self.nse_table)

        st.write("")
        st.write("")

    # Function to display the stock selectbox.
    def stocks_selectbox(self):
        st.write("")
        st.write("")

        st.markdown("### BSE Stocks Volume History")
        if self.symbols:
            self.symbol = st.selectbox("Choose a stock", self.symbols)
            return self.symbol
        else:
            st.error("Error in fetching the BSE stocks list.")

    def stocks_graph_display(self):
        st.write("")
        st.write("")
        volume_df = get_graph_dataframe(self.symbol)

        st.markdown(f'### Volumes for {self.symbol}')
        if not volume_df.empty:
            st.line_chart(volume_df)
        else:
            st.error("No data available for the selected stock.")

