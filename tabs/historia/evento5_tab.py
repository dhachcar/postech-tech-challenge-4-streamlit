import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento5Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Primavera Árabe (2010-2012)]', divider='blue')
            st.markdown('''
                A Primavera Árabe foi uma série de protestos e movimentos populares que eclodiram em diversos países do Oriente Médio e do Norte da África, a partir de 2010. Originados principalmente por insatisfações sociais, políticas e econômicas, esses levantes exigiam reformas políticas, democracia e direitos humanos. Iniciando na Tunísia, os protestos rapidamente se espalharam para países como Egito, Líbia, Síria, Iêmen e Bahrein, entre outros. Embora tenham gerado mudanças significativas em alguns lugares, como a queda de governos autocráticos, em outros resultaram em conflitos prolongados, guerras civis e instabilidade política, com consequências de longo prazo para toda a região.
            ''')