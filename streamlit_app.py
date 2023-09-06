import streamlit as st
import pandas as pd

@st.cache
def load_data():
    # Load data here
    return pd.read_csv("survey_data.csv")

data = load_data()

# Conversion dictionary
conversion_dict = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5
}

# Convert the data using the dictionary
for col in data.columns[2:]:
    data[col] = data[col].map(conversion_dict)

# Filtering the data
st.sidebar.header('Filter Data')
regions = st.sidebar.multiselect('Region', data['Region'].unique())
roles = st.sidebar.multiselect('Role', data['Role'].unique())

filtered_data = data[data['Region'].isin(regions) & data['Role'].isin(roles)]

# Display data
st.write(filtered_data)

# Navigation
nav = st.sidebar.radio('', ['Home', 'Navigate to'])

if nav == 'Navigate to':
    st.header("Summary Statistics")
    
    # Calculate the average scores for each section
    policy_design_avg = filtered_data[data.columns[2:12]].mean(axis=1).mean()
    st.write(f"Average score for Policy Design: {policy_design_avg:.2f}")
    
    process_avg = filtered_data[data.columns[12:22]].mean(axis=1).mean()
    st.write(f"Average score for Process: {process_avg:.2f}")
    
    people_avg = filtered_data[data.columns[22:32]].mean(axis=1).mean()
    st.write(f"Average score for People: {people_avg:.2f}")
