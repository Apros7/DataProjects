import streamlit as st
import random
import matplotlib.pyplot as plt
import pickle
import datetime
import copy

st.set_page_config(layout="wide")

# Education: Folkeskole +5, STX +5, Kurser på DTU +8
# Programming skills: Books +2, Kurser +1, Online +2
# Business skills: Books +5

levels = {
        'Education': 18,
        'Programming Skills': 5,
        'Business Skills': 5,
        'Momentum': 0,
        'Health': 20,
        'Sleep': 10,
        'Social Media Usage': 100,
    }

history = {"Baseline": levels, "2023-07-17": levels, "2023-07-18": levels, "2023-07-19": levels}

def days_left_in_year():
    current_date = datetime.date.today()
    last_day_of_year = datetime.date(current_date.year + 1, 1, 1) - datetime.timedelta(days=1)
    days_left = (last_day_of_year - current_date).days
    return days_left

def generate_random_levels():
    return {
        'Education': random.randint(0, 10),
        'Programming Skills': random.randint(10, 20),
        'Business Skills': random.randint(90, 100),
        'Momentum': random.randint(70, 80),
        'Health': random.randint(20, 50),
        'Sleep': random.randint(0, 10),
        'Social Media Usage': 100,
    }

def save_levels(levels):
    with open("levels.pkl", "wb") as f:
        pickle.dump(levels, f)

def load_levels():
    with open("levels.pkl", "rb") as f:
        return pickle.load(f)

def save_history(history):
    with open("history.pkl", "wb") as f:
        pickle.dump(history, f)

def load_history():
    with open("history.pkl", "rb") as f:
        return pickle.load(f)

def save_checks(checks):
    with open("checks.pkl", "wb") as f:
        pickle.dump(checks, f)

def load_checks():
    with open("checks.pkl", "rb") as f:
        return pickle.load(f)

def save_main_goal_number(numbers):
    with open("main_goal_number.csv", "w") as f:
        for number in numbers:
            f.write(str(int(number)) + "\n")

def load_main_goal_number():
    return [int(x) for x in open("main_goal_number.csv", "r").readlines()]

#save_history(history)

def plot_skill_graph(skill_levels):
    st.markdown(f'<h3 style="font-size:25px;text-align:center">Current skill levels:</h3>', unsafe_allow_html=True)

    skills = list(skill_levels.keys())
    levels = list(skill_levels.values())

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(skills, levels)
    #ax.set_xlabel('Skills')
    ax.set_ylabel('Levels')
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
    st.markdown(f'<h3 style="font-size:25px;text-align:center">Skill Development over Time:</h3>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(8, 6))

    for key in list(skill_levels.values())[0]:
        values = [level[key] for level in skill_levels.values()]
        ax.plot(range(len(values)), values, label=key)

    #ax.set_xlabel('Time')
    ax.set_ylabel('Levels')
    
    time_points = list(skill_levels.keys())
    num_ticks = min(10, len(time_points)) 
    step_size = len(time_points) // num_ticks
    x_ticks = time_points[::step_size]

    ax.set_xticks(range(len(x_ticks)))
    ax.set_xticklabels(x_ticks)
    plt.xticks(rotation=20)
    ax.legend()
    st.pyplot(fig)

def level_up(text, key, skill_levels):
    skill_levels[key] += 1
    with open("reviews.csv") as f:
        f.write(key, skill_levels[key], text)
    return skill_levels

def process_levels(skill_levels, checks):
    representative_key = ["Momentum", "Sleep", "Momentum", "Health", "Momentum", "Social Media Usage"]
    values = [1, 1, 1, 1, 1, -1]
    for key, check, value in zip(representative_key, checks, values):
        if check: skill_levels[key] += value
        else: skill_levels[key] -= value
    return adjust_levels(skill_levels)

def adjust_levels(skill_levels): 
    for k, v in skill_levels.items():
        if v < 0: skill_levels[k] = 0
        if v > 100: skill_levels[k] = 100
    return skill_levels

def save_skill_levels(skill_levels, date, history):
    history[date] = skill_levels
    save_history(history)

def main_goal_info():
    days_left_this_year = days_left_in_year()
    main_goal_current_numbers = load_main_goal_number()
    main_goal_final_numbers = [5, 100, 600]
    st.markdown(f'<h3 style="font-size:25px;text-align:center">Main goals this year:</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: 
        st.markdown(f'<h3 style="font-size:18px;text-align:center">{days_left_this_year} days left this year.</h3>', unsafe_allow_html=True)
        st.progress(1 - days_left_this_year/365)
        st.divider()
        st.markdown(f'<h3 style="font-size:18px;text-align:center">100 days wake up before 6 AM</h3>', unsafe_allow_html=True)
        st.progress(main_goal_current_numbers[1]/main_goal_final_numbers[1])
    with col2:
        st.markdown(f'<h3 style="font-size:18px;text-align:center">5 schools to use GrammatikTAK!</h3>', unsafe_allow_html=True)
        st.progress(main_goal_current_numbers[0]/main_goal_final_numbers[0])
        st.divider()
        st.markdown(f'<h3 style="font-size:18px;text-align:center">600 hours on GrammatikTAK!</h3>', unsafe_allow_html=True)
        st.progress(main_goal_current_numbers[2]/main_goal_final_numbers[2])
    st.divider()
    col1, col2, col3 = st.columns(3)
    options = ["Schools", "6 AM wake up", "Hours"]
    with col1: goal_to_update = st.selectbox("Select goal to update: ", options)
    with col2: number = st.number_input("Add to current value", value = 0, step = 1)
    with col3: st.write(""); st.write(""); update = st.button("Update")
    if update:
        main_goal_current_numbers[options.index(goal_to_update)] += number
        save_main_goal_number(main_goal_current_numbers)
        st.experimental_rerun()

def main():
    st.title('Game of Life - Skill Development')

    history = load_history()
    checks = load_checks()
    skill_levels = list(history.values())[-1]

    columns = st.columns(len(skill_levels))
    items = list(skill_levels.items())
    for i in range(len(items)):
        with columns[i]:
            skill, level = items[i]
            st.markdown(f'<h3 style="font-size:20px">{skill}: {level}</h3>', unsafe_allow_html=True)
            st.progress(level)

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        main_goal_info()
    with col2:
        plot_skill_graph(skill_levels)
    with col3:
        plot_skill_time_graph(history)

    st.divider()

    st.header("Daily habits:")

    # Maybe only today
    date = str(st.date_input("Please select the date you want to look at: "))
    if date not in history: history[date] = skill_levels
    if date == list(history.keys())[-1]: skill_levels = list(history.values())[-2]
    save_history(history)

    st.write("Please select which habits you did today. This will impact your levels.")

    habits_lst = ["2 hours of work on grammatiktak", "8.5 hours in bed", "Wake up before 6 am", 
                  "30 min of exercise", "30 min of reading", "Less than 2 hours on social media"]
    habits = {habit: False for habit in habits_lst}

    if date in checks:
        habits = {habit: checks[date][i] for i, habit in enumerate(habits_lst)}

    check_values = []
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3, col1, col2, col3]
    for i, habit in enumerate(habits):
        with columns[i]:
            check_values.append(st.checkbox(habit, habits[habit]))

    save = st.button("Submit")
    if save:
        checks[date] = check_values
        save_checks(checks)
        # History is automatically updated, which is really weird
        old_hist = copy.deepcopy(history)
        skill_levels = process_levels(skill_levels, check_values)
        save_skill_levels(skill_levels, date, old_hist)
        st.experimental_rerun()

    st.divider()

    st.header("Level up:")
    skill_to_level_up = st.selectbox("Choose which skill to level up:", list(skill_levels.keys()))

    questions = {
        'Education': ["Did you finish a school course (>100 hours)?"],
        'Programming Skills': ["Did you read a programming book?", "Did you learn a new programming language?", "Did you finish a programming course?"],
        'Business Skills': ["Did you finish a business course or book?", "Did you learn a new business releated skill?"],
        'Momentum': [],
        'Health': [],
        'Sleep': [],
        'Social Media Usage': [],
    }

    st.markdown(f'<h3 style="font-size:30px">You can level up if you can answer yes to any of these questions: </h3>', unsafe_allow_html=True)
    related_questions = questions[skill_to_level_up]
    if len(related_questions) == 0:
        st.write("This skill can only be leveled up through habits :-).")
    else:
        columns = st.columns(len(related_questions))

        for i in range(len(related_questions)):
            with columns[i]:
                st.markdown(f'<h3 style="font-size:20px">{related_questions[i]}</h3>', unsafe_allow_html=True)

        review = st.text_input("Please write a few lines on what you have achieved: ")
        submit_button = st.button("Level up")
        if submit_button:
            old_hist = copy.deepcopy(history)
            new_skill_levels = level_up(review, skill_to_level_up, skill_levels)
            save_skill_levels(new_skill_levels, date, history)
            st.experimental_rerun()



if __name__ == '__main__':
    main()
