from libs.base_page import BasePage
from random import randint
import streamlit as st
from time import sleep
class Monitoring(BasePage):
    
    def __init__(self):
        super().__init__()
        self.st = st
    def draw(self) -> None:
        cols = self.st.columns(3, gap="large")
        with cols[0]:
            self.st.header("Humidity (%)")
            self.st.write(f"{round(self.st.session_state['humidity_value'],2)} %")
            bar = self.st.progress(int(self.st.session_state["humidity_value"]), "")
            if "min_value_humidity" in self.st.session_state and "max_value_humidity" in self.st.session_state:
                if self.st.session_state["humidity_value"] < self.st.session_state["min_value_humidity"]:
                    self.st.info('The humidity level is under the minimum seted', icon="ℹ️")
                if self.st.session_state["humidity_value"] > self.st.session_state["max_value_humidity"]:
                    self.st.warning('The humidity level is above the maximum seted', icon="ℹ️")
        with cols[1]:
            self.st.header("Temperature (°C)")
            self.st.subheader(f"{round(self.st.session_state['temperature_value'], 1)} °C")
            if "min_value_temperature" in self.st.session_state and "max_value_temperature" in self.st.session_state:
                if self.st.session_state["temperature_value"] < self.st.session_state["min_value_temperature"]:
                    self.st.info('The temperature level is under the minimum seted', icon="ℹ️")
                if self.st.session_state["temperature_value"] > self.st.session_state["max_value_temperature"]:
                    self.st.warning('The temperature level is above the maximum seted', icon="ℹ️")
                if (self.st.session_state["temperature_value"] > self.st.session_state["min_value_temperature"]) and (self.st.session_state["temperature_value"] < self.st.session_state["max_value_temperature"]):
                    self.st.success("The temperature level is normal!", icon="✔")
        with cols[2]:
            self.st.header("Brightness (%)")
            self.st.write(f"{round(self.st.session_state['brightness_value'],2)} %")
            bar = self.st.progress(int(self.st.session_state["brightness_value"]), "")
            if "min_value_brightness" in self.st.session_state and "max_value_brightness" in self.st.session_state:
                if self.st.session_state["brightness_value"] < self.st.session_state["min_value_brightness"]:
                    self.st.info('The brightness level is under the minimum seted', icon="ℹ️")
                if self.st.session_state["brightness_value"] > self.st.session_state["max_value_brightness"]:
                    self.st.warning('The brightness level is above the maximum seted', icon="ℹ️")
        
        self.generate_random_numbers(self.st.session_state["humidity_value"], self.st.session_state["temperature_value"], self.st.session_state["brightness_value"])
        sleep(2)
        self.st.rerun()    
        
            
    def generate_random_numbers(self, humidity: float, temperature: float, brightness: float) -> None:
        value_h = randint(1, 25)
        value_t = randint(1, 10)
        value_b = randint(1, 25)
        #Humidity
        if self.to_sum(): humidity+= (humidity*value_h)/100
        else: humidity-= (humidity*value_h)/100
        #Temperature
        if self.to_sum(): temperature+= (temperature*value_t)/100
        else: temperature-= (temperature*value_t)/100
        #Brigthness
        if self.to_sum(): brightness+= (brightness*value_b)/100
        else: brightness-= (brightness*value_b)/100
        
        if humidity > 100:
            humidity = 100
        if brightness > 100:
            humidity = 100
        self.st.session_state["humidity_value"] = humidity
        self.st.session_state["temperature_value"] = temperature
        self.st.session_state["brightness_value"] = brightness
        
    def to_sum(self) -> bool:
        num = randint(0,1)
        if num == 1:
            return True
        return False
        
        
monitoring = Monitoring()
monitoring.draw()