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

# Filter data according to the selected section
if selected_section == "All sections":
    filtered_data = data
else:
    filtered_data = data[data["PDD Section"] == selected_section]

# Only show content for the selected anchor
if selected_anchor == "Policy Design Framework/Process":
    st.header("Policy Design Framework/Process")
    for question in data.columns[2:12]:  # First 10 questions
        value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
        value_counts.columns = ['Response', 'Count']
        fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
        st.plotly_chart(fig)

elif selected_anchor == "Memo Writing":
    st.header("Memo Writing")
    for question in data.columns[12:15]:  # Next 3 questions
        value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
        value_counts.columns = ['Response', 'Count']
        fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
        st.plotly_chart(fig)

elif selected_anchor == "Oral Briefing":
    st.header("Oral Briefing")
    for question in data.columns[15:18]:  # Final 3 questions
        value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
        value_counts.columns = ['Response', 'Count']
        fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
        st.plotly_chart(fig)
