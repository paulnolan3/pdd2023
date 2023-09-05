# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter using radio buttons
sections = ["All sections"] + list(data["PDD Section"].unique())
selected_section = st.sidebar.radio("Select PDD Section", sections)

if selected_section == "All sections":
    filtered_data = data
else:
    filtered_data = data[data["PDD Section"] == selected_section]

# Define Likert scale ordering and numerical mapping
likert_order = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
likert_mapping = {
    "Strongly Agree": 5,
    "Agree": 4,
    "Neutral": 3,
    "Disagree": 2,
    "Strongly Disagree": 1
}

# Visualize distribution of responses for each question
for question in data.columns[2:-2]:  # Excluding the open-ended questions
    value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
    value_counts.columns = ['Response', 'Count']
    
    # Calculate average response for the question
    avg_response = filtered_data[question].map(likert_mapping).mean()
    
    # Plot
    fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}")
    fig.add_trace(go.Scatter(x=[avg_response], y=[value_counts['Count'].max()], mode='markers+text', text=['Avg'], textposition='top center'))
    st.plotly_chart(fig)

# Display random responses for the open-ended questions
for question in data.columns[-2:]:
    st.write(f"Random Responses for: {question}")
    sample_responses = filtered_data[question].dropna().sample(5)
    for idx, response in sample_responses.iteritems():
        st.write(f"- {response}")
