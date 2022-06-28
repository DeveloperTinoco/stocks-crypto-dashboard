import streamlit as st

# Set page config
st.set_page_config(
    page_title="Stocks/Crypto Dashboard",
    page_icon="📊",
    initial_sidebar_state="collapsed",
)

# Read style.css to customize contents
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Page title
st.markdown(
    """
    <h1 style="text-align: center;">📊 Stocks/Crypto Dashboard 📊</h1>
    """, unsafe_allow_html=True)

# Display information using Markdown
st.markdown(
    """
    
    ## Page 1 📈
    
    > Top 50 Stocks By **Percentage Gains**
    
    ## Page 2 📉
    
    > Top 50 Stocks By **Percentage Losses**
    
    ## Page 3 💰
    
    > Top 50 Cryptocurrencies By **Market Cap**
    
    ---
    
    ## Technologies Used
    
    
    - Python == 3.10.2
    - Streamlit == 1.10.0
    - Plotly == 5.8.2
    - Pandas == 1.4.2
    - Requests_HTML == 0.10.0
    - YFinance == 0.1.70
    
        
    ---
    
    ## Information & Features
    
    
    This web app obtains stock/crypto data from Yahoo Finanace.
    
    The data is dynamically obtained in order to be up to date.

    Charts are created using the data & users can compare multiple tickers.
    
    Filters can be applied/changed when comparing data.
    
    Date ranges can be changed to view data between certain dates.
    
    """, unsafe_allow_html=True)