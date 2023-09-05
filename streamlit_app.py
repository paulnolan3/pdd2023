# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter using radio buttons
sections = ["All sections"] + list(data["PDD Section"].unique())
selected_section = st.sidebar.radio("Select PDD Section", sections)

if selected_section == "All sections":
    filtered_data = data
else:
    filtered_data = data[data["PDD Section"] == selected_section]

# Define Likert scale ordering
likert_order = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

# Visualize distribution of responses for the "Policy Design Framework/Process" section
st.header("Policy Design Framework/Process")
for question in data.columns[2:12]:  # First 10 questions
    value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
    value_counts.columns = ['Response', 'Count']
    fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
    st.plotly_chart(fig)

# Visualize distribution of responses for the "Memo Writing" section
st.header("Memo Writing")
for question in data.columns[12:15]:  # Next 3 questions
    value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
    value_counts.columns = ['Response', 'Count']
    fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
    st.plotly_chart(fig)

# Visualize distribution of responses for the "Oral Briefing" section
st.header("Oral Briefing")
for question in data.columns[15:18]:  # Final 3 questions
    value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
    value_counts.columns = ['Response', 'Count']
    fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
    st.plotly_chart(fig)

# Display random responses for the open-ended questions
for question in data.columns[-2:]:
    st.write(f"Random Responses for: {question}")
    available_responses = filtered_data[question].dropna()
    sample_size = min(len(available_responses), 5)
    sample_responses = available_responses.sample(sample_size)
    for idx, response in sample_responses.iteritems():
        st.write(f"- {response}")
