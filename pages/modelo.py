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

    st.markdown(
        """
        Prever o preço do barril de petróleo é um desafio crítico para muitos setores, e tanto o :blue[Prophet] quanto a :blue[LSTM] são ferramentas valiosas nessa tarefa. O :blue[Prophet], criado pela :blue[Meta], é conhecido por sua acessibilidade e habilidade em lidar com padrões sazonais complexos, enquanto a :blue[LSTM], fornecido pela junção do :blue[Tensorflow & Keras], é uma forma de rede neural recorrente, se destaca em capturar relações de longo prazo nos dados, algo essencial em mercados voláteis como o do petróleo. Ambos os modelos oferecem abordagens poderosas e complementares para entender e antecipar as flutuações no mercado de energia, fornecendo insights valiosos para tomadas de decisão.
    """
    )

    tab0, tab1 = st.tabs(tabs=["Meta Prophet", "Tensorflow Keras LSTM"])

    ModeloProphetTab(tab0)
    ModeloLSTMTab(tab1)
