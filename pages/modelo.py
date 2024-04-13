import streamlit as st
from tabs.modelo.lstm_tab import ModeloLSTMTab
from tabs.modelo.prophet_tab import ModeloProphetTab
from util.constantes import TITULO_MODELO, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_MODELO}]")

    tab0, tab1 = st.tabs(tabs=['Prophet', 'LSTM'])

    ModeloProphetTab(tab0)
    ModeloLSTMTab(tab1)

    # TODO: no modelo, permitir a escolha do horizonte de previsão
    # TODO: mostrar o grafico de treino + previsao do horizonte
    # TODO: mostrar o quanto a previsao vai se perdendo conforme o tempo passa