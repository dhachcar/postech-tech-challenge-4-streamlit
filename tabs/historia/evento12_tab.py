import streamlit as st
from tabs.tab import TabInterface

class HistoriaEvento12Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':one::two: :blue[Conflito Rússia-Ucrânia (2022~)]', divider='blue')
            st.markdown('''
                A escalada do conflito entre a Ucrânia e a Rússia, iniciada em fevereiro de 2022, foi caracterizada por uma intensificação das tensões na região leste da Ucrânia, especialmente nas áreas controladas por separatistas pró-Rússia em Donetsk e Lugansk. Os confrontos diretos entre as forças ucranianas e as tropas russas resultaram em relatos de mortes e um aumento significativo nos preços do gás e do petróleo, ampliando as preocupações sobre os impactos econômicos e geopolíticos da crise.
            ''')