import streamlit as st
from streamlit_option_menu import option_menu
import snowflake.connector

#Layout
st.set_page_config(
    page_title="CV LIMS - Library Information Management Systems",
    layout="wide",
    initial_sidebar_state="expanded")


st.header("Welcome to the CV's MS Library")

with st.sidebar:
    selected = option_menu('MS LIMS', ['Login', 'Manage Account','Transact Books', 'View Books', 'Logout'], 
        icons=['unlock','eyes', 'play-btn','search','info-circle'],menu_icon='intersect', default_index=0)

st.text("User ID / Email")
st.text("Password")
