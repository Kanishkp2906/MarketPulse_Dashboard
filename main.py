import streamlit as st
from dashboard import Dashboard
from stocks_page import StocksPage

def main():
    st.sidebar.title("Navigation")
    sidebar_button = st.sidebar.radio("Go to:", ['Dashboard','Stock Prices'])

    if sidebar_button == "Dashboard":
        dashboard = Dashboard()
        dashboard.gold_price_display()
        dashboard.silver_price_display()
        dashboard.usd_rate_display()
        dashboard.metal_city_rates()

    elif sidebar_button == "Stock Prices":
        sp = StocksPage()
        sp.stocks_table_display()
        if sp.stocks_selectbox():
            sp.stocks_graph_display()

if __name__ == "__main__":
    main()