import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento9Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':nine: :blue[Grande produção e baixa demanda (2015)]', divider='blue')
            st.markdown('''
                Em 2015, houve uma situação de grande produção de petróleo em meio a uma baixa demanda global. Isso foi resultado da decisão da Organização dos Países Exportadores de Petróleo (OPEP) de manter a produção, combinada com um enfraquecimento da demanda devido a desacelerações econômicas em várias partes do mundo. O excesso de oferta de petróleo levou a uma queda acentuada nos preços do petróleo bruto, o que afetou severamente as economias dos países produtores de petróleo e provocou uma reestruturação significativa no setor de energia em escala global.
            ''')