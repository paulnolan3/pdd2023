import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import io

# Display logo at the top of the sidebar
st.sidebar.image("logo.png", use_column_width=True)

# Load the data
data = pd.read_excel("PPD_Competencies.xlsx")

# Sidebar for PDD Section filter using radio buttons
sections = ["All sections"] + list(data["PDD Section"].unique())
selected_section = st.sidebar.radio("Select PDD Section", sections)

# Sidebar buttons for navigating to sections
selected_anchor = st.sidebar.radio("Navigate to", ["Policy Design Framework/Process", "Memo Writing", "Oral Briefing"])

# Define Likert scale ordering and corresponding colors
likert_order = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
colors = {'Strongly Agree': 'green', 'Agree': 'lightgreen', 'Neutral': 'gray', 'Disagree': 'lightcoral', 'Strongly Disagree': 'red'}

# Filter data according to the selected section
if selected_section == "All sections":
    filtered_data = data
else:
    filtered_data = data[data["PDD Section"] == selected_section]

# Function to plot individual chart
def plot_chart(question):
    # Break long titles into two lines
    display_title = "<br>".join([question[i:i+30] for i in range(0, len(question), 30)])
    
    value_counts = filtered_data[question].value_counts().reindex(likert_order).reset_index()
    value_counts.columns = ['Response', 'Count']
    fig = px.bar(value_counts, x='Response', y='Count', title=f"Responses for: {display_title}", color='Response', color_discrete_map=colors)
    fig.update_layout(margin=dict(l=150))  # Adjust the left margin to give titles more space

    # Convert the figure to PNG image
    img_bytes = pio.to_image(fig, format="png")
    buf = io.BytesIO(img_bytes)
    buf.seek(0)
    
    st.plotly_chart(fig)
    st.download_button(label="Download PNG", data=buf, file_name=f"{question}.png", mime="image/png")

# Show content based on the selected anchor
if selected_anchor == "Policy Design Framework/Process":
    st.header("Policy Design Framework/Process")
    for question in data.columns[2:12]:  # First 10 questions
        plot_chart(question)

elif selected_anchor == "Memo Writing":
    st.header("Memo Writing")
    for question in data.columns[12:15]:  # Next 3 questions
        plot_chart(question)

elif selected_anchor == "Oral Briefing":
    st.header("Oral Briefing")
    for question in data.columns[15:18]:  # Final 3 questions
        plot_chart(question)
