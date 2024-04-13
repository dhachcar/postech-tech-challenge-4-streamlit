import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento3Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':three: :blue[Guerra do Iraque (2003-2011)]', divider='blue')
            st.markdown('''
                A Guerra do Iraque, também conhecida como Guerra do Golfo II, começou em março de 2003 quando uma coalizão liderada pelos Estados Unidos invadiu o país. O objetivo principal era remover Saddam Hussein do poder, alegando que ele possuía armas de destruição em massa e apoiava o terrorismo. Depois que o regime de Hussein foi derrubado, o conflito evoluiu para uma longa e complexa guerra de guerrilha, que resultou em muitas vidas perdidas e deixou um legado de instabilidade na região do Oriente Médio.
            ''')