import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento5Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Primavera Árabe (2010-2012)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')