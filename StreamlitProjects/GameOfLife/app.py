import streamlit as st
import random
import matplotlib.pyplot as plt
import pickle

levels = {
        'Education': 10,
        'Programming Skills': 10,
        'Business Skills': 5,
        'Momentum': 0,
        'Health': 40,
        'Sleep': 10
    }

def generate_random_levels():
    return {
        'Education': random.randint(0, 10),
        'Programming Skills': random.randint(10, 20),
        'Business Skills': random.randint(90, 100),
        'Momentum': random.randint(70, 80),
        'Health': random.randint(20, 50),
        'Sleep': random.randint(0, 10),
    }

def save_levels(levels):
    with open("levels.pkl", "wb") as f:
        pickle.dump(levels, f)

save_levels(levels)

def load_levels():
    with open("levels.pkl", "rb") as f:
        return pickle.load(f)

def save_history():
    pass

def load_history():
    with open("history.pkl", "rb") as f:
        return pickle.load(f)

def plot_skill_graph(skill_levels):
    skills = list(skill_levels.keys())
    levels = list(skill_levels.values())

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(skills, levels)
    #ax.set_xlabel('Skills')
    ax.set_ylabel('Levels')
    ax.set_title('Current skill levels')
    ax.set_yticks([x for x in range(0, 101, 10)])
    plt.xticks(rotation=20)
    st.pyplot(fig)

def generate_skill_progression():
    progression = {}
    for i in range(50):
        progression[i] = generate_random_levels()
    return progression

# Function to plot the graph
def plot_skill_time_graph(skill_levels):
    fig, ax = plt.subplots(figsize=(8, 6))

    skill_levels = generate_skill_progression()

    for key in list(skill_levels.values())[0]:
        values = [level[key] for level in skill_levels.values()]
        ax.plot(range(len(values)), values, label=key)

    ax.set_xlabel('Time')
    ax.set_ylabel('Levels')
    ax.set_title('Skill Development over Time')
    
    time_points = list(skill_levels.keys())
    num_ticks = min(10, len(time_points)) 
    step_size = len(time_points) // num_ticks
    x_ticks = time_points[::step_size]

    time_labels = [f'Time {tp}' for tp in x_ticks]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks)
    plt.xticks(rotation=45)
    ax.legend()
    st.pyplot(fig)

# Main function to run the Streamlit app
def main():
    st.set_page_config(layout="wide")
    st.title('Game of Life - Skill Development')

    # Generate random initial skill levels
    skill_levels = load_levels()

    # Display skill levels as bars
    columns = st.columns(len(skill_levels))
    items = list(skill_levels.items())
    for i in range(len(items)):
        with columns[i]:
            skill, level = items[i]
            st.subheader(skill)
            st.progress(level)

    col1, col2 = st.columns(2)
    with col1:
        plot_skill_graph(skill_levels)
    with col2:
        plot_skill_time_graph(skill_levels)

    st.divider()

    st.header("Daily habits:")

if __name__ == '__main__':
    main()
