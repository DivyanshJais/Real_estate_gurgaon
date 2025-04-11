import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")
st.write("# Select the options from the Side bar")

st.sidebar.success("Select a demo above.")