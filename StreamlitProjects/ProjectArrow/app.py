import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pickle

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
    <p style='text-align: center; color: rgb(80,80,80); font-size: 21px;'>Current score: </p>
    <h2 style='text-align: center; color: rgb(40,40,40);'>Tech Advancements</h2>
    <p style='text-align: center; color: rgb(80,80,80); font-size: 21px;'>Measures: Work & Revenue</p>
    <p style='text-align: center; color: rgb(80,80,80); font-size: 21px;'>Current score: </p>
    """, unsafe_allow_html=True)

with col2: 

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Ressource Allocation</h1>
    """, unsafe_allow_html=True)

    st.divider()

    allocation = {
        "Sleep": 8.75,
        "School/Work": 6,
        "Eat": 1.75,
        "Relax": 2,
        "Projects": 3,
        "Knowledge": .5,
        "Exercise": 2
    }

    # plot actual allocation - 30 day average

    x = [k for k, v in allocation.items()]
    y = [v for k, v in allocation.items()]

    fig, ax = plt.subplots()
    ax.bar(x, y)

    ax.set_xlabel('Activity')
    ax.tick_params(axis='x', labelrotation=22)
    ax.set_ylabel('Hours')
    y_max = max(y) + 1
    y_ticks = [i for i in range(int(y_max)+1)]
    ax.set_yticks(y_ticks)
    ax.set_title('Ressource Allocation')

    st.pyplot(fig)

with col3: 

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Results</h1>
    """, unsafe_allow_html=True)

    st.divider()

    # results = {
    #     "Sleep score": get_sleep_score(),
    #     "Activity score": get_activity_score(),
    #     "Work score": get_work_score(), 
    #     "Revenue score": get_revenue_score()
    # }

st.divider()

col1, col2 = st.columns(2)

def load_cur_all(date):
    all_dates = pickle.load(open("/Users/lucasvilsen/Desktop/DataProjects/StreamlitProjects/ProjectArrow/cur_res_all.pickle", "rb"))
    if date in all_dates: return all_dates[date]
    current_allocation = {
        "Sleep": 0,
        "School/Work": 0,
        "Eat": 0,
        "Relax": 0,
        "Projects": 0,
        "Knowledge": 0,
        "Exercise": 0,
    }
    return current_allocation

def save_cur_all(date, data):
    all_dates = pickle.load(open("/Users/lucasvilsen/Desktop/DataProjects/StreamlitProjects/ProjectArrow/cur_res_all.pickle", "rb"))
    all_dates[date] = data
    with open("/Users/lucasvilsen/Desktop/DataProjects/StreamlitProjects/ProjectArrow/cur_res_all.pickle", "wb") as file:
        pickle.dump(all_dates, file)

with col1:

    st.markdown("""
    <h1 style='text-align: center; color: rgb(40,40,40);'>Time Tracking: </h1>
    """, unsafe_allow_html=True)

    st.divider()

    col11, col12, col13, col14 = st.columns(4)
    with col11: date = str(st.date_input("Date to look at"))
    with col12: theme = st.selectbox("Select activity", x)
    with col13: value = st.number_input("Type hours to add")
    with col14: st.write(""); st.write(""); to_add = st.button("Press to add")

    current_allocation = load_cur_all(date)

    x = [k for k, v in current_allocation.items()]
    y = [v for k, v in current_allocation.items()]

    fig, ax = plt.subplots()
    ax.bar(x, y)

    ax.set_xlabel('Activity')
    ax.tick_params(axis='x', labelrotation=22)
    ax.set_ylabel('Hours')
    y_max = max(y) + 1
    y_ticks = [i for i in range(int(y_max)+1)]
    ax.set_yticks(y_ticks)
    ax.set_title('Current Ressource Allocation')

    if to_add:
        current_allocation[theme] += value
        save_cur_all(date, current_allocation)
        st.experimental_rerun()
    st.pyplot(fig)

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
    sleep_length_diff = max(0, optimal_sleep_length - sleep_length_minutes)
    sleep_begin_diff = max(0, sleep_begin_minutes - optimal_sleep_begin)
    exponential = (100 - sleep_length_diff + 100 - sleep_begin_diff)**2 / 100 
    return exponential