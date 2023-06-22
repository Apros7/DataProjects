import streamlit as st
import numpy as np
import time

st.title("""
STOCK 1 V 1:
""")

Tickers = ["AAPL", "MCD", "TSLA", "MSFT"]

st.select

import yfinance as yf
stock_info = yf.Ticker('TSLA').info

price_history = yf.Ticker('TSLA').history(period='max', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1d', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
time_series = list(price_history['Open'])

progress_bar = st.progress(0)
status_text = st.empty()
divisor = 20
last_rows = time_series[:divisor]
chart = st.line_chart(last_rows)

for i in range(1, len(time_series)//divisor):
    new_rows = time_series[i*divisor:i*divisor+divisor]
    progress_value = i/(len(time_series)//divisor)
    status_text.text(f"{round(progress_value*100, 2)}% Complete")
    chart.add_rows(new_rows)
    progress_bar.progress(progress_value)
    last_rows = new_rows
    time.sleep(0.03)

status_text.text(f"100% Complete")
# progress_bar.empty()