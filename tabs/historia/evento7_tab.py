import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento7Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Conflito na Síria (2011~)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')