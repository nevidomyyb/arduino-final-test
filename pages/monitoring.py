from libs.base_page import BasePage
from random import randint
import streamlit as st

class Monitoring(BasePage):
    
    def __init__(self):
        super().__init__()
        self.st = st
    def draw(self) -> None:
        cols = self.st.columns(3, gap="large")
        with cols[0]:
            self.st.header("Humidity (%)")
            bar = self.st.progress(0, "")
            
    def generate_random_numbers(self, humidity: float, temperature: float, brightness: float) -> float:
        value_h = randint(1, 10)
        value_t = randint(1, 10)
        value_b = randint(1, 10)
        #Humidity
        if self.to_sum(): humidity+= humidity + (humidity*value_h)/100
        else: humidity-= (humidity*value_h)/100
        #Temperature
        
    def to_sum(self) -> bool:
        num = randint(0,1)
        if num == 1:
            return True
        return False
        
        
monitoring = Monitoring()
monitoring.draw()