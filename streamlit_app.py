# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    st.write(f"Responses for: {question}")
    fig, ax = plt.subplots()
    filtered_data[question].value_counts().sort_index().plot(kind="bar", ax=ax)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

# Display PDD Section distribution with a pie chart
st.write("PDD Section Distribution")
fig, ax = plt.subplots()
data["PDD Section"].value_counts().plot(kind="pie", ax=ax, autopct='%1.1f%%')
st.pyplot(fig)

# Display random responses for the open-ended questions
for question in data.columns[-2:]:
    st.write(f"Random Responses for: {question}")
    sample_responses = filtered_data[question].dropna().sample(5)
    for idx, response in sample_responses.iteritems():
        st.write(f"- {response}")
