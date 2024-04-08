import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento2Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Atentados terroristas nos EUA (2001)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')