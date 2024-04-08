import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento4Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Crise financeira global (2007-2008)]', divider='blue')
            st.markdown('''
                Abaixo, a arquitetura deste projeto:
            ''')