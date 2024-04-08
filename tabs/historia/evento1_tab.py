import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento1Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Guerra do Golfo (1990-1991)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')