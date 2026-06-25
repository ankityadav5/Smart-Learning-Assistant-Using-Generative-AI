from dotenv import load_dotenv
load_dotenv()

import streamlit as st

api_key = st.secrets.get(
    "GEMINI_API_KEY",
    os.getenv("GEMINI_API_KEY")
)
