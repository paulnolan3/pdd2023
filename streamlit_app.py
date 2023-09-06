def break_title(title, max_length=30):
    """
    Break a title into lines, ensuring that words are not split and each line does not exceed max_length.
    """
    words = title.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        if len(current_line + ' ' + word) <= max_length:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return "<br>".join(lines)

def plot_chart(question):
    # Break long titles into lines without cutting off words
    display_title = break_title(question)
    
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
