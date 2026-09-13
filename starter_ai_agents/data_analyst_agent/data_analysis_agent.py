import io

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq


load_dotenv()


# -----------------------------
# Streamlit Setup
# -----------------------------

st.set_page_config(
    page_title="📊 Data Analysis Agent",
    page_icon="📊",
)

st.title("📊 Data Analysis Agent")
st.write("Upload a CSV and let AI analyze your dataset.")


# -----------------------------
# Agent
# -----------------------------

agent = Agent(
    name="Data Analysis Agent",
    model=Groq(id="openai/gpt-oss-20b"),
    instructions=[
        "You are a data analysis assistant.",
        "Analyze the dataset information provided by Python.",
        "Explain findings clearly and concisely.",
        "Identify important patterns and insights.",
        "Do not invent values.",
        "Use only the information provided to you.",
    ],
    markdown=True,
)


# -----------------------------
# Upload CSV
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"],
)


if uploaded_file:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("CSV loaded successfully!")

    # -----------------------------
    # Dataset Preview
    # -----------------------------

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
    )


    # -----------------------------
    # Dataset Information
    # -----------------------------

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isna().sum().sum()))


    # -----------------------------
    # Generate Analysis
    # -----------------------------

    if st.button("🔍 Analyze Dataset", type="primary"):

        with st.spinner("Analyzing dataset..."):

            # Basic statistics
            numeric_summary = df.describe().to_string()

            # Column information
            column_info = df.dtypes.to_string()

            # Missing values
            missing_values = df.isna().sum().to_string()

            prompt = f"""
            Analyze this dataset.

            Dataset shape:
            {df.shape}

            Column types:
            {column_info}

            Missing values:
            {missing_values}

            Numerical statistics:
            {numeric_summary}

            Provide:

            ## Overview
            Explain what the dataset contains.

            ## Key Insights
            Identify important patterns or observations.

            ## Data Quality
            Mention missing values or obvious data quality issues.

            ## Recommendations
            Suggest useful next analysis steps.

            Do not invent information.
            """

            response = agent.run(prompt)


        st.subheader("🤖 AI Analysis")

        st.markdown(response.content)