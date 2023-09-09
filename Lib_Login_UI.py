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
        icons=['unlock','info-circle', 'play-btn','search','lock'],menu_icon='intersect', default_index=0)


if selected=="Login":
    #Header
    st.title('Welcome to CV MS LIMS')
    st.subheader('*Please login to the system as as Admin or a User*')
    st.text("User ID / Email")
    st.text("Password")
    st.divider()


#Manage Account Page
if selected=="Manage Account":
    st.subheader('Account Management Actions')
    with st.container():
        col1,col2,col3=st.columns(3)
        with col1:
            st.button("Create user account");
        with col2:
            st.button("Modify user account");
        with col3:            
            st.button("Delete user account");
    
    st.divider()

#Search Page
if selected=="Transact Books":
    st.subheader('Please chooise option to either borrow or return books')
    st.button("Borrow Books");
    st.button("Return Books");
    st.button("Pay Penalty");
    st.divider()
    
#Search Page
if selected=="View Books":
    st.subheader('Search or View Books in Catalog & Check availability')
    st.button("Search Catalog");
    st.button("View Recent Books");
    st.button("Popular Titles");
    st.button("Popular Authors");
    st.button("Popular Genre");
    st.divider()

#Logout Page
if selected=="Logout":
    st.subheader('Thank you for visiting CV MS LIMS')
    st.text("Please close browsers for safety");
    st.divider()
