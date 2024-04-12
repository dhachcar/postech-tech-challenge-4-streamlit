import streamlit as st
from tabs.tab import TabInterface

class IntroPetroleoBrentTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Petróleo Brent]', divider='blue')
            st.markdown('''
                O petróleo Brent é uma referência internacional para o preço do petróleo bruto, utilizado como padrão para determinar os preços de compra e venda em todo o mundo. Originário do Mar do Norte, o petróleo Brent é um tipo de petróleo leve e doce, de alta qualidade, que é amplamente negociado nos mercados internacionais de commodities. Seu preço é influenciado por uma série de fatores, incluindo a oferta e demanda globais, eventos geopolíticos, políticas de produção da OPEP e condições econômicas mundiais.
                A relevância do petróleo Brent como padrão internacional se deve à sua ampla disponibilidade e qualidade consistente, tornando-o uma referência confiável para transações comerciais e contratos futuros. Os preços do petróleo Brent são frequentemente citados como indicadores-chave da saúde e estabilidade da economia global, afetando uma variedade de setores, desde transporte e energia até alimentação e manufatura. Como resultado, flutuações significativas nos preços do petróleo Brent podem ter impactos substanciais em economias nacionais e na política internacional.
            ''')