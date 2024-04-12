import streamlit as st
from tabs.tab import TabInterface

class IntroEIATab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Energy Information Administration (EIA)]', divider='blue')
            st.markdown('''
                A Energy Information Administration (EIA) é uma agência do governo dos Estados Unidos responsável por coletar, analisar e disseminar informações sobre energia, incluindo dados sobre produção, consumo, preços e reservas de petróleo, gás natural, carvão, energia elétrica e renovável.\n\n
                Fundada em 1977, a EIA desempenha um papel crucial na elaboração de políticas energéticas, fornecendo informações precisas e imparciais para governos, empresas, pesquisadores e o público em geral. Suas projeções e relatórios são amplamente utilizados para orientar investimentos, avaliar tendências de mercado e planejar políticas públicas relacionadas à energia nos Estados Unidos e globalmente.\n\n
                Para este projeto, foi criado uma conta de acesso à base da EIA e requisitado acesso à sua API. Com a liberação em mãos, foram consultados todos os dados históricos do EIA a respeito do preço do barril de petróleo Brent. A base em si consiste em dados desde maio/1987 até os dias atuais.
            ''')