import streamlit as st
class BasePage():
    
    def __init__(self):
        st.set_page_config(
            initial_sidebar_state="collapsed", 
            page_title="Mini-test logic programming",
            page_icon="✅",
            layout="wide"
        )
        st.title("Menu")
        cols = st.columns(2)
        
        if cols[0].button("Monitoring"):
            st.switch_page('pages/monitoring.py')
        if cols[1].button("Configurations"):
            st.switch_page('pages/configurations.py')
        st.divider()