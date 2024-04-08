import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento11Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Recuperação econômica pós-COVID (2021~)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')