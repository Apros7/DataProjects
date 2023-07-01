# inspiration: https://neal.fun/where-does-the-day-go/

import streamlit as st
import pandas as pd

st.markdown("<h1 align='center'>Time Visualizer</h1>", unsafe_allow_html=True)

"""
### See how much time you are actually using on each task throughout the day:
"""

st.markdown("<h1 align='center'><font color='lightcoral'><b>Your Typical Day</b></font></h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    work = st.slider("Amount of work in a day (hrs)", 1, 22, value=8, key="work_slider", help="Select the amount of work in hours")
with col2:
    sleep = st.slider("Amount of sleep in a day (hrs)", 1, 22, value=8, key="sleep_slider", help="Select the amount of sleep in hours")
with col3:
    home = st.slider("Amount of time home in a day (hrs)", 1, 22, value=8, key="home_slider", help="Select the amount of time spent at home in hours")

if work + sleep + home > 24 or work + sleep + home < 24:
    st.markdown("<h3 align='center'><font color='grey'><b>Sliders must equal to 24</b></font></h3>", unsafe_allow_html=True)

df = pd.DataFrame