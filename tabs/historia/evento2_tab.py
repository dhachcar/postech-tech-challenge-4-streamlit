import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento2Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':two: :blue[Atentados terroristas nos EUA (2001)]', divider='blue')
            st.markdown('''
                O atentado de 11 de setembro de 2001 foi uma série de ataques terroristas coordenados pela organização extremista Al-Qaeda contra os Estados Unidos. Aviões comerciais foram sequestrados e deliberadamente direcionados às Torres Gêmeas do World Trade Center em Nova York, além do Pentágono em Washington, D.C. Um quarto avião caiu na Pensilvânia após os passageiros tentarem retomar o controle. Este evento resultou na perda de milhares de vidas e teve um impacto significativo na política global, segurança internacional e estratégias antiterrorismo.
            ''')