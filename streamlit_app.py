# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter using radio buttons
sections = ["All sections"] + list(data["PDD Section"].unique())
selected_section = st.sidebar.radio("Select PDD Section", sections)

# Sidebar buttons for navigating to sections
selected_anchor = st.sidebar.radio("Navigate to", ["Policy Design Framework/Process", "Memo Writing", "Oral Briefing"])

# Define Likert scale ordering
likert_order = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

# Only show content for the selected anchor
if selected_anchor == "Policy Design Framework/Process":
    st.header("Policy Design Framework/Process")
    # ... [rest of the Policy Design code]

elif selected_anchor == "Memo Writing":
    st.header("Memo Writing")
    # ... [rest of the Memo Writing code]

elif selected_anchor == "Oral Briefing":
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
