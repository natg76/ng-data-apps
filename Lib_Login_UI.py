import streamlit as st
import snowflake.connector

#Layout
st.set_page_config(
    page_title="CV LIMS - Library Information Management Systems",
    layout="wide",
    initial_sidebar_state="expanded")


st.header("Welcome to the CV's MS Library")


st.sidebar.text("Login")
st.sidebar.text("Account Management")
st.sidebar.text("Transact Books")
st.sidebar.text("View Books")
st.sidebar.text("Logout")

st.text("User ID / Email")
st.text("Password")
