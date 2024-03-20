import streamlit as st
from libs.base_page import BasePage

class Configurations(BasePage):
    
    def __init__(self):
        super().__init__()
        self.st = st
        
    def draw(self) -> None:
        cols = self.st.columns(3, gap="large")
        
        with cols[0]:
            self.st.header("Humidity sensor (%)")
            min_value_humidity = self.st.number_input("Minimum value of humidity", value=0.0, step=0.01, min_value=0.0, max_value= 100.0)
            max_value_humidity = self.st.number_input("Maximum value of humidity", value=100.0, step=0.01,max_value=100.0, min_value= 0.0)
        with cols[1]:
            self.st.header("Temperature sensor (°C)")
            min_value_temperature = self.st.number_input("Minimum value of temperature", value=0.0, step=0.01)
            max_value_temperature = self.st.number_input("Maximum value of temperature", value=100.0, step=0.01)
        with cols[2]:
            self.st.header("Brightness sensor (%)")
            min_value_brightness = self.st.number_input("Minimum value of brightness", value=0.0, step=0.01, min_value=0.0, max_value=100.0)
            max_value_brightness = self.st.number_input("Maximum value of brightness", value=100.0, step=0.01,max_value=100.0, min_value=0.0)
            
        if self.st.button("Save"):
            variables = {
                "min_value_humidity": min_value_humidity,
                "max_value_humidity": max_value_humidity,
                "min_value_temperature": min_value_temperature,
                "max_value_temperature": max_value_temperature,
                "min_value_brightness": min_value_brightness,
                "max_value_brightness": max_value_brightness
            }
            for variable_name, value in variables.items():
                self.st.session_state[variable_name] = value
            self.st.success("Configurations saved!")


configurations = Configurations()
configurations.draw()
        
    