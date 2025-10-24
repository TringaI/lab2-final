import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

st.title("Study Hours Dashboard")
st.write("This page displays visualizations based on data from your CSV and JSON files.")

data = {}
try:
    json_path = os.path.join(os.path.dirname(__file__), "..", "data.json")
    with open(json_path, "r") as f:
        data = json.load(f)
except Exception as e:
    st.error(f"Error loading JSON file: {e}")
    st.stop()

chart_title = data.get("chart_title", "My Chart")
points = data.get("data_points", [])
df_json = pd.DataFrame(points)

st.divider()
st.header("Dynamic Bar Chart from JSON 📊")

if "scale" not in st.session_state:
    st.session_state.scale = 100

st.session_state.scale = st.slider(
    "Adjust overall intensity (%)", 50, 150, st.session_state.scale
)

df_json["Adjusted Value"] = df_json["value"] * (st.session_state.scale / 100)

fig_bar = px.bar(
    df_json,
    x="label",
    y="Adjusted Value",
    color="label",
    title=f"{chart_title} (Adjusted by Slider)",
    labels={"label": "Day of Week", "Adjusted Value": "Study Hours"},
)

st.write(
    "This interactive bar chart shows the study hours for each day of the week based on the data stored in the JSON file. "
    "Use the slider above to adjust the overall intensity, which dynamically scales all the values."
)
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()
st.header("Dynamic Line Chart from CSV 📈")

if os.path.exists("data.csv"):
    csv_df = pd.read_csv("data.csv")
    max_rows = len(csv_df)

    use_slider = st.checkbox("Use slider to select number of rows?", value=True)

    if use_slider:
        num_rows = st.slider(
            "Select number of CSV rows to display",
            1,
            max_rows,
            max_rows
        )
    else:
        num_rows = st.number_input(
            "Enter number of CSV rows to display",
            min_value=1,
            max_value=max_rows,
            value=max_rows,
            step=1
        )

    filtered_df = csv_df.head(num_rows)

    fig_line = px.line(
        filtered_df,
        x="label",
        y="value",
        markers=True,
        title="CSV Data Line Chart",
        labels={"label": "Day of Week", "value": "Value"},
    )

    st.write(
        "This line chart shows how your recorded values change over time. You can choose how many entries to display using the slider or the number input. This allows you to focus on recent activity, review the full dataset, or explore trends over specific periods."
    )
    st.plotly_chart(fig_line, use_container_width=True)
else:
    st.warning("No CSV data found. Please submit some data on the Survey page first.")

st.divider()
st.header("Static Pie Chart from JSON 🥧")

fig_pie = px.pie(
    df_json,
    names="label",
    values="value",
    title="Proportion of Study Hours by Day",
    labels={"label": "Day of Week", "value": "Study Hours"},
)

st.write(
    "This pie chart shows the proportion of values for each category, giving you a quick overview of how different categories compare to each other. It helps you see which categories dominate and how your entries are distributed."
)
st.plotly_chart(fig_pie, use_container_width=True)
