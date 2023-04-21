import yfinance as yf
import streamlit as st

st.write("""
# Stock Ticker Web App for Indian Stocks which have returned more than 20% for the past 5 years

""")

st.write(""" # Pidilite Industries Stock Ticker """)
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'PIDILITIND.NS'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='5Y', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write("""====================""")

st.write(""" # Bajaj Finance Stock Ticker """)

tickerSymbol = 'BAJFINANCE.NS'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='5y', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write("""====================""")

st.write(""" # GMM Pfaudler Stock Ticker """)

tickerSymbol = 'BAJFINANCE.NS'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='5y', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)