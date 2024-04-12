import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento6Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Guerra Civil na Líbia (2011)]', divider='blue')
            st.markdown('''
                A guerra civil da Líbia foi um conflito que eclodiu em 2011, como parte dos movimentos da Primavera Árabe, levando à queda do regime autocrático de Muammar Gaddafi. No entanto, após a deposição de Gaddafi, o país mergulhou em um período de turbulência e instabilidade política, com grupos armados rivais competindo pelo controle do território e dos recursos. A disputa entre as diferentes facções levou a uma guerra civil prolongada, marcada por violência generalizada, violações dos direitos humanos e intervenções estrangeiras. Essa situação resultou em um cenário de fragmentação política e divisão territorial, com o país dividido entre governos rivais e grupos armados, contribuindo para um estado de caos e incerteza que persiste até os dias de hoje.
            ''')