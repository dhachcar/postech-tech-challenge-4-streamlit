import streamlit as st
from util.constantes import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_INTRODUCAO}]")

    tab0, tab1, tab2, tab3 = st.tabs(
        tabs=[
            "Análise demográfica",
            "Análise clínica",
            "Machine Learning: Ensemble",
            "Machine Learning: Não-supervisionado",
        ]
    )
