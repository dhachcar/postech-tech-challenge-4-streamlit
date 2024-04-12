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
                A Guerra do Golfo, ocorrida entre agosto de 1990 e fevereiro de 1991, foi um conflito militar que teve origem na invasão do Kuwait pelo Iraque, liderado por Saddam Hussein. A coalizão internacional liderada pelos Estados Unidos, com o apoio de países como Reino Unido, França e Arábia Saudita, interveio para expulsar as forças iraquianas do Kuwait. A guerra foi marcada por intensos combates terrestres, aéreos e navais, culminando na libertação do Kuwait e na imposição de sanções econômicas ao Iraque.
            ''')