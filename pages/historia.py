import streamlit as st
from util.constantes import TITULO_HISTORIA, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_HISTORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_HISTORIA}]")

    # colocar grafico com todos os pontos historicos
    # colocar tabs contando um pouco sobre cada ocorrencia