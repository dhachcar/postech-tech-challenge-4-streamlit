import plotly.graph_objs as go
import pandas as pd
import streamlit as st
from util.constantes import TITULO_PRINCIPAL
from util.layout import output_layout
import warnings
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(
    ":blue[Análise histórica do petróleo Brent: analisando o seu passado e prevendo o seu futuro]",
    divider="blue",
)
st.markdown(
    """
    Este projeto tem como propósito analisar as flutuações históricas do preço do petróleo Brent e criar um modelo de machine learning para prever seus valores futuros. O petróleo Brent, como uma referência internacional essencial para os preços do petróleo, é amplamente utilizado em transações comerciais e contratos futuros em âmbito global. Compreender as tendências passadas e identificar padrões nos dados históricos do preço do petróleo Brent oferece insights valiosos para investidores, empresas e formuladores de políticas energéticas.\n\n
    Ao explorar os dados históricos do preço do petróleo Brent, realizaremos análises estatísticas para compreender melhor os padrões e tendências ao longo do tempo. Este processo incluirá a identificação de fatores que influenciam significativamente o preço do petróleo, como oferta e demanda, geopolítica e condições econômicas globais. Além disso, utilizaremos técnicas de visualização de dados para destacar padrões e correlações relevantes, o que nos permitirá desenvolver insights mais aprofundados sobre o comportamento do mercado de petróleo.\n\n
    Após a análise, é criado um modelo de machine learning voltado para séries temporais que será responsável por prever o preço futuro do barril de petróleo Brent.
"""
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    Prever o preço futuro do barril de petróleo do tipo BRENT
"""
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    Falar que os dados foram puxados do EIA via API
"""
)
