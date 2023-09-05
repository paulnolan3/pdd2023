# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter using radio buttons and anchor links
sections = ["All sections"] + list(data["PDD Section"].unique())
selected_section = st.sidebar.radio("Select PDD Section", sections)

# Sidebar anchor links
st.sidebar.markdown("[Policy Design Framework/Process](#policy-design)")
st.sidebar.markdown("[Memo Writing](#memo-writing)")
st.sidebar.markdown("[Oral Briefing](#oral-briefing)")

if selected_section == "All sections":
    filtered_data = data
else:
    filtered_data = data[data["PDD Section"] == selected_section]

# Define Likert scale ordering
likert_order = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

# Visualize distribution of responses for the "Policy Design Framework/Process" section
st.markdown("<a id='policy-design'></a>", unsafe_allow_html=True)
st.header("Policy Design Framework/Process")
# ... [rest of the Policy Design code]

# Visualize distribution of responses for the "Memo Writing" section
st.markdown("<a id='memo-writing'></a>", unsafe_allow_html=True)
st.header("Memo Writing")
# ... [rest of the Memo Writing code]

# Visualize distribution of responses for the "Oral Briefing" section
st.markdown("<a id='oral-briefing'></a>", unsafe_allow_html=True)
st.header("Oral Briefing")
# ... [rest of the Oral Briefing code]

# Display random responses for the open-ended questions
for question in data.columns[-2:]:
    st.write(f"Random Responses for: {question}")
    available_responses = filtered_data[question].dropna()
    sample_size = min(len(available_responses), 5)
    sample_responses = available_responses.sample(sample_size)
    for idx, response in sample_responses.iteritems():
        st.write(f"- {response}")
