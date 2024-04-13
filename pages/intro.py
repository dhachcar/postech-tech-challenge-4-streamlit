import streamlit as st
from tabs.intro.eia_tab import IntroEIATab
from tabs.intro.ipea_tab import IntroIPEATab
from tabs.intro.petroleo_brent_tab import IntroPetroleoBrentTab
from util.constantes import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_INTRODUCAO}]")

    st.markdown(
        """
        Nesta introdução, são descritos alguns tópicos importantes para o entendimento do projeto, dentre eles oque é o petróleo Brent, a EIA e o IPEA.
    """
    )

    tab0, tab1, tab2 = st.tabs(
        tabs=[
            "Petróleo Brent",
            "Instituto de Pesquisa Econômica Aplicada (IPEA)",
            "Energy Information Administration (EIA)",
        ]
    )

    IntroPetroleoBrentTab(tab0)
    IntroIPEATab(tab1)
    IntroEIATab(tab2)
