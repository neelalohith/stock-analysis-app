import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Simple Stock Price App
the stock closing price and volume of Google are displayed below
""")
tickersymbol = 'GOOGL'
tickerData = yf.Ticker(tickersymbol)
tickerdf = tickerData.history(period='10d',start='2010-5-22',end='2023-6-19')
st.write("""
# Closing Price
""")
st.line_chart(tickerdf.Close)
st.write("""
# Volume Price 
""")
st.line_chart(tickerdf.Volume)

st.write("""
# The stock closing price and volume of Apple are displayed below
""")
tickersymbol1= 'AAPL'
tickerData1 = yf.Ticker(tickersymbol1)
tickerdf1 = tickerData1.history(period='10d',start='2010-5-28',end='2023-6-17')
st.write("""
## Closing Price
""")
st.line_chart(tickerdf1.Close)
st.write("""
## Volume Price 
""")
st.line_chart(tickerdf1.Volume)
