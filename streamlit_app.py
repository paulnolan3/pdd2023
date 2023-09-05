# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter
selected_section = st.sidebar.selectbox("Select PDD Section", data["PDD Section"].unique())
filtered_data = data[data["PDD Section"] == selected_section]

# Display summary statistics for the selected section
st.write(f"Summary Statistics for {selected_section}")
st.write(filtered_data.describe())

# Visualize distribution of responses for each question
for question in data.columns[2:-2]:  # Excluding the open-ended questions
    fig = px.bar(filtered_data[question].value_counts().reset_index(), 
                 x='index', 
                 y=question, 
                 title=f"Responses for: {question}", 
                 labels={'index': 'Responses', question: 'Count'})
    st.plotly_chart(fig)

# Display PDD Section distribution with a pie chart
fig = px.pie(data, names='PDD Section', title='PDD Section Distribution')
st.plotly_chart(fig)

# Display random responses for the open-ended questions
for question in data.columns[-2:]:
    st.write(f"Random Responses for: {question}")
    sample_responses = filtered_data[question].dropna().sample(5)
    for idx, response in sample_responses.iteritems():
        st.write(f"- {response}")
