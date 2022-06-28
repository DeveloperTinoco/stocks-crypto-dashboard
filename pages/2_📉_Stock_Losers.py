from operator import iconcat
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from functions import get_data, display_metrics, display_candlesticks

# Set page title and icon
st.set_page_config(
    page_title='Stock Losers',
    page_icon='📉',
)

# Read style.css to customize contents
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

url = 'https://finance.yahoo.com/losers?offset=0&count=50'
css_selector = '[data-field=regularMarketChangePercent]'

# Page title
st.markdown('<h1 style="text-align: center;">📉 Stock Losers 📉</h1>', unsafe_allow_html=True)

# Get date of one month ago from whatever today's date is
last_month = date.today() - timedelta(days = 30)

# Call cache function and list filters available
stock_losers = get_data(url, css_selector)
losers_filters = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

# Create multiselect dropdown with retrieved stocks and filters
select_l_stocks = st.multiselect('Select Stocks:', stock_losers)
l_filter = st.selectbox("Select Chart Filter:", losers_filters)

# Create date inputs for chart history
start = st.date_input('From', value = pd.to_datetime(last_month))
end = st.date_input('To', value = pd.to_datetime('today'))

# Display chart when ticker is selected with filters
if len(select_l_stocks) > 0:
    df = yf.download(select_l_stocks, start, end)[l_filter]
    st.line_chart(df)
    
# Take dictionary and select the top three and put in new dictionary
first3pairs = {k: stock_losers[k] for k in list(stock_losers)[:3]}

# Markdown seperator
st.markdown('---')

# Metrics title
st.markdown('<h1 style="text-align: center;">Top 3 Stocks By Percentage Losses</h1>', unsafe_allow_html=True)

# Call function to display metrics
three_tickers = display_metrics(first3pairs)

# Call function for each candlestick chart
fig1 = display_candlesticks(three_tickers[0])
fig2 = display_candlesticks(three_tickers[1])
fig3 = display_candlesticks(three_tickers[2])

# Update layout to include stock name on side
fig1.update_layout(yaxis_title=f'{three_tickers[0]} Stock')
fig2.update_layout(yaxis_title=f'{three_tickers[1]} Stock')
fig3.update_layout(yaxis_title=f'{three_tickers[2]} Stock')

# Display candlestick charts
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)