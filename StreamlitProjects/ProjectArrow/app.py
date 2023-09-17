import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Set app title and page configuration
st.set_page_config(
    page_title="Beautiful Streamlit App",
    page_icon="🏹",
    layout="wide"
)

st.markdown("<p style='font-size: 70px; text-align: center; color: rgb(60,120,60);'>Project Arrow!</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Objectives</h1>
    """, unsafe_allow_html=True)

    st.divider()
    
    st.markdown("""
    <h2 style='text-align: center; color: rgb(40,40,40);'>Longevity</h2>
    <p style='text-align: center; color: rgb(80,80,80); font-size: 21px;'>Measures: Sleep & Activity</p>
    <h2 style='text-align: center; color: rgb(40,40,40);'>Tech Advancements</h2>
    <p style='text-align: center; color: rgb(80,80,80); font-size: 21px;'>Measures: Work & Revenue</p>
    """, unsafe_allow_html=True)

with col2: 

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Ressource Allocation</h1>
    """, unsafe_allow_html=True)

    st.divider()

with col3: 

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Results</h1>
    """, unsafe_allow_html=True)

    st.divider()

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Time Tracking: </h1>
    """, unsafe_allow_html=True)

    st.divider()

with col2: 

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Result Tracking: </h1>
    """, unsafe_allow_html=True)

    st.divider()


def to_minutes(value):
    v1, v2 = value.split(":")
    return int(v1) * 60 + int(v2)

def get_sleep_score(sleep_length, sleep_begin):
    optimal_sleep_begin = 21 * 60
    optimal_sleep_length = 8 * 60 + 45
    sleep_length_minutes = to_minutes(sleep_length)
    sleep_begin_minutes = to_minutes(sleep_length)
    sleep_begin_diff = max()