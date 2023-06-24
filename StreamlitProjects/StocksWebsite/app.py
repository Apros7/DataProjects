import streamlit as st
import pandas as pd
import time



st.markdown("<h1 style='text-align: center; color: grey;'>STOCK 1 V 1:</h1>", unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)

Tickers = ["AAPL", "MCD", "TSLA", "MSFT"]

with col1:  
    st.markdown("<h3 style='text-align: center; color: blue;'>Choose your fighter</h3>", unsafe_allow_html=True)
    stock1 = st.selectbox("Stock 1:", ["AAPL", "MCD", "TSLA", "MSFT"])

with col2:
    st.markdown("<h3 style='text-align: center; color: lightblue;'>Choose your challenger</h3>", unsafe_allow_html=True)
    stock2 = st.selectbox("Stock 2:", ["AAPL", "MCD", "TSLA", "MSFT"])

st.divider()

import yfinance as yf

stock1_info = yf.Ticker(stock1).info

periods = ["1d", "1mo", "1y", "max"]
selected_period = st.selectbox("Interval:", options=periods)
period_to_interval = {"1d": "5m", "1mo": "60m", "1y": "1h", "max": "1wk"}

price_history1 = yf.Ticker(stock1).history(period=selected_period, interval=period_to_interval[selected_period], actions=False)
price_history2 = yf.Ticker(stock2).history(period=selected_period, interval=period_to_interval[selected_period], actions=False)
# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

time_series1 = list(price_history1['Open'])
time_series2 = list(price_history2['Open'])

min_len = min(len(time_series1), len(time_series2))
time_series1 = time_series1[-min_len:]
time_series2 = time_series2[-min_len:]

data = {stock1: time_series1, stock2: time_series2}
df = pd.DataFrame(data)

progress_bar = st.progress(0)
status_text = st.empty()
divisor = 20
last_rows = df[:divisor]
chart = st.line_chart(last_rows)

for i in range(1, len(time_series1)//divisor):
    new_rows = df[i*divisor:i*divisor+divisor]
    progress_value = i/(len(time_series1)//divisor)
    status_text.text(f"{round(progress_value*100, 2)}% Complete")
    chart.add_rows(new_rows)
    progress_bar.progress(progress_value)
    last_rows = new_rows
    time.sleep(0.03)

status_text.text(f"100% Complete")
progress_bar.progress(100)

st.divider()
st.header("Key Metrics:")
col1, col2 = st.columns(2)
st.write("""
Could be:
- Variation
- Average increase in price for last 6 months
- Profit growth for 3 years
- Revenue growth for 3 years
""")

st.divider()
st.header("Final Scores:")