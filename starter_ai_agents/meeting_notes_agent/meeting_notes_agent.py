import streamlit as st
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq


load_dotenv()


# -----------------------------
# Streamlit Setup
# -----------------------------

st.set_page_config(
    page_title="📝 Meeting Notes Agent",
    page_icon="📝",
)

st.title("📝 Meeting Notes Agent")
st.write("Turn a meeting transcript into clear, structured notes.")


# -----------------------------
# Agent
# -----------------------------

agent = Agent(
    name="Meeting Notes Agent",
    model=Groq(id="openai/gpt-oss-20b"),
    instructions=[
        "You are a professional meeting notes assistant.",
        "Analyze the meeting transcript provided by the user.",
        "Create concise and useful meeting notes.",
        "Extract the main discussion points.",
        "Identify important decisions.",
        "Identify action items and responsible people.",
        "Include deadlines when mentioned.",
        "Do not invent information.",
        "If an owner or deadline is not mentioned, say 'Not specified'.",
    ],
    markdown=True,
)


# -----------------------------
# Input
# -----------------------------

transcript = st.text_area(
    "Meeting Transcript",
    height=300,
    placeholder="Paste your meeting transcript here...",
)


# -----------------------------
# Generate Notes
# -----------------------------

if st.button("Generate Meeting Notes", type="primary"):

    if not transcript.strip():

        st.warning("Please enter a meeting transcript.")

    else:

        with st.spinner("Analyzing meeting..."):

            response = agent.run(
                f"""
                Convert the following meeting transcript into
                structured meeting notes.

                Meeting Transcript:
                {transcript}

                Include these sections:

                ## Meeting Summary

                ## Key Discussion Points

                ## Key Decisions

                ## Action Items

                Keep the notes concise.
                Do not invent information.
                """
            )

        st.success("Meeting notes generated!")

        st.markdown(response.content)