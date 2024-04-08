import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento12Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Conflito Rússia-Ucrânia (2022~)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')