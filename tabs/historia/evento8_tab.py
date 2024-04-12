import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento8Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[OPEP mantém ritmo de produção (2014)]', divider='blue')
            st.markdown('''
                Em 2014, a Organização dos Países Exportadores de Petróleo (OPEP) decidiu manter sua produção de petróleo inalterada, apesar do excesso de oferta no mercado global. Essa decisão foi tomada principalmente para manter a participação de mercado da OPEP e pressionar os produtores de petróleo de xisto nos Estados Unidos, cuja produção havia aumentado significativamente. No entanto, essa estratégia acabou levando a uma queda drástica nos preços do petróleo, afetando profundamente a economia de muitos países dependentes do petróleo e causando instabilidade nos mercados globais de energia.
            ''')