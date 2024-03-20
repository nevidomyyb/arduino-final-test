import streamlit as st
from random import uniform
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
        
        if "humidity_value" not in st.session_state:
            st.session_state["humidity_value"] = round(uniform(5, 70), 2)
        if "temperature_value" not in st.session_state:
            st.session_state["temperature_value"] = round(uniform(0, 70), 2)
        if 'brightness_value' not in st.session_state:
            st.session_state["brightness_value"] = round(uniform(0, 70), 2)
        
        st.divider()