# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter using radio buttons
sections = ["All sections"] + list(data["PDD Section"].unique())
selected_section = st.sidebar.radio("Select PDD Section", sections)

# Sidebar buttons for navigating to sections or pages
selected_anchor = st.sidebar.radio("Navigate to", ["Policy Design Framework/Process", "Memo Writing", "Oral Briefing", "Summary Statistics"])

# Define Likert scale ordering and corresponding colors
likert_order = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
colors = {'Strongly Agree': 'green', 'Agree': 'lightgreen', 'Neutral': 'gray', 'Disagree': 'lightcoral', 'Strongly Disagree': 'red'}

# Filter data according to the selected section
if selected_section == "All sections":
    filtered_data = data
else:
    filtered_data = data[data["PDD Section"] == selected_section]

# Show content for the selected anchor or page
if selected_anchor == "Policy Design Framework/Process":
    st.header("Policy Design Framework/Process")
    for question in data.columns[2:12]:  # First 10 questions
        value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
        value_counts.columns = ['Response', 'Count']
        fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}", color='Response', color_discrete_map=colors)
        st.plotly_chart(fig)

elif selected_anchor == "Memo Writing":
    st.header("Memo Writing")
    for question in data.columns[12:15]:  # Next 3 questions
        value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
        value_counts.columns = ['Response', 'Count']
        fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}", color='Response', color_discrete_map=colors)
        st.plotly_chart(fig)

elif selected_anchor == "Oral Briefing":
    st.header("Oral Briefing")
    for question in data.columns[15:18]:  # Final 3 questions
        value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
        value_counts.columns = ['Response', 'Count']
        fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {question}", color='Response', color_discrete_map=colors)
        st.plotly_chart(fig)

elif selected_anchor == "Summary Statistics":
    st.header("Summary Statistics")

    # Calculate and display the average scores for each section
    policy_design_avg = filtered_data[data.columns[2:12]].mean(axis=1).mean()
    memo_writing_avg = filtered_data[data.columns[12:15]].mean(axis=1).mean()
    oral_briefing_avg = filtered_data[data.columns[15:18]].mean(axis=1).mean()

    st.write(f"Average Score for Policy Design Framework/Process: {policy_design_avg:.2f}")
    st.write(f"Average Score for Memo Writing: {memo_writing_avg:.2f}")
    st.write(f"Average Score for Oral Briefing: {oral_briefing_avg:.2f}")
