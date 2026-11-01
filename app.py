from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Social Hub",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the app looks like a native mobile app.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 480px;}
      iframe {border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "static" / "index.html").read_text(encoding="utf-8")
components.html(html, height=860, scrolling=False)
