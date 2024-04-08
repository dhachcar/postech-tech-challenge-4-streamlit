import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento9Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Grande produção e baixa demanda (2015)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')