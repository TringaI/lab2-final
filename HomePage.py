import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="🏠",
)

st.title("Welcome to the Data Dashboard! 📊")

st.write("""
This application is designed to collect and visualize data.
You can navigate to the different pages using the sidebar on the left.
""")

st.write("### How to use this app:")

st.write("""
- **Survey Page**: Go here to input new data into our CSV file.
""")
if st.button("Go to Survey Page 📝"):
    st.experimental_set_query_params(page="Survey")
    st.experimental_rerun()

st.write("""
- **Visuals Page**: Go here to see the data visualized in different graphs.
""")
if st.button("Go to Visuals Page 📈"):
    st.experimental_set_query_params(page="Visuals")
    st.experimental_rerun()

st.write("""
This project is part of CS 1301's Lab 2.
""")
