

import streamlit as st

st.set_page_config(
    page_title="Homepage",  
    page_icon="🏠",         
)

st.title("Welcome to the Data Dashboard! 📊")

st.write("""
This application is designed to collect and visualize data. You can navigate to the different pages using the sidebar on the left.

### How to use this app:
- **Survey Page**: Go here to input new data into the CSV file.
- **Visuals Page**: Go here to see the data visualized in different graphs.

This project is part of CS 1301's Lab 2.
""")

st.image("images/welcome_image.png")
