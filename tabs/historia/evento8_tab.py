import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento8Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[OPEP mantém ritmo de produção (2014)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')