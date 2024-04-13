import streamlit as st
from tabs.tab import TabInterface

class ModeloLSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.write('teste2')