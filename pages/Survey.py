import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to add your data to the dataset.")

if not os.path.exists("data.csv"):
    pd.DataFrame(columns=["label", "value"]).to_csv("data.csv", index=False)
    
#I restricted user inputs to weekdays to ensure that the data represents meaningful information, allowing the graphs to accurately reflect study patterns. But the inputs still accept strings
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

with st.form("survey_form"):
    category_input = st.text_input("Enter a category (e.g., Monday):")
    value_input = st.text_input("How many hours did you study on Monday (number):")
    submitted = st.form_submit_button("Submit Data")

    if submitted:
        errors = []

        normalized_input = category_input.strip().capitalize()

        if normalized_input not in valid_days:
            errors.append("Invalid input. Please enter a valid weekday (e.g., Monday).")

        if not value_input.replace('.', '', 1).isdigit():
            errors.append("Invalid input. Please enter a numeric value (e.g., 2, 2.5).")

        if errors:
            for error in errors:
                st.error(error)
        else:
            val = float(value_input)
            if val.is_integer():
                val = int(val)

            new_row = pd.DataFrame([[normalized_input, val]], columns=["label", "value"])

            if os.path.exists("data.csv"):
                new_row.to_csv("data.csv", mode="a", header=False, index=False)
            else:
                new_row.to_csv("data.csv", mode="w", header=True, index=False)

            st.success("Your data has been submitted!")
            st.write(f"You entered: **Category:** {normalized_input}, **Value:** {val}")

st.divider()
st.header("Current Data in CSV")

if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    current_data_df = pd.read_csv('data.csv')
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
