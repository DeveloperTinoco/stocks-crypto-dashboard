import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from datetime import date, timedelta
from requests_html import HTMLSession

# Retrieve data from specified url using specified css selector and store the retrieved data in a dictionary and return it
@st.cache
def get_data(url, css_selector):
    session = HTMLSession()
    tickers = {}

    gainers = session.get(url)
    link_content = gainers.html.find('tr.simpTblRow')

    for content in link_content:
        a_selector = content.find('a', first=True)
        price_selector = content.find('[data-field=regularMarketPrice]', first=True)
        percentage_selector = content.find(css_selector, first=True)

        tickers[a_selector.text] = [
            price_selector.text, percentage_selector.text]

    return tickers

# Display the metrics of the top 3 stocks/cryptos for the appropriate page (gains, losses, marketcap) by taking the dictionary
# we created and taking the first three elements and then displaying them in their own column
def display_metrics(first3pairs):
    three_tickers = []
    prices = []
    percents = []

    for key, value in first3pairs.items():
        three_tickers.append(key)
        prices.append(value[0])
        percents.append(value[1])

    col1, col2, col3 = st.columns(3)
    col1.metric(f'${prices[0]}', three_tickers[0], percents[0])
    col2.metric(f'${prices[1]}', three_tickers[1], percents[1])
    col3.metric(f'${prices[2]}', three_tickers[2], percents[2])
    
    return three_tickers

# Display the candlestick charts of the top 3 stock/cryptos from the display_metrics function
@st.cache(allow_output_mutation=True)
def display_candlesticks(ticker):
    three_months = date.today() - timedelta(days=90)
    begin = pd.to_datetime(three_months)
    today = pd.to_datetime('today')
    
    df = yf.download(ticker, begin, today)

    df = pd.DataFrame(df)

    fig = go.Figure(data=[go.Candlestick(x = df.index,
                                      open=df['Open'],
                                      close=df['Close'],
                                      high=df['High'],
                                      low=df['Low'])])

    return fig