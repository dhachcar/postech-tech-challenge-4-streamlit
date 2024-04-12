import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento7Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Conflito na Síria (2011~)]', divider='blue')
            st.markdown('''
                O conflito na Síria, em curso desde 2011, é uma crise humanitária devastadora que já deixou milhões de pessoas deslocadas e causou uma terrível perda de vidas. Originado de protestos pacíficos contra o governo, o conflito rapidamente se transformou em uma guerra civil complexa, envolvendo múltiplas facções, incluindo o governo sírio, rebeldes, grupos extremistas e intervenções estrangeiras. Bombardeios, ataques aéreos e cercos a áreas civis têm sido comuns, causando um sofrimento indescritível para a população síria, com acesso limitado a alimentos, água e cuidados médicos. Apesar de esforços diplomáticos e tréguas temporárias, a resolução do conflito parece distante
            ''')