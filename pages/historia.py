import streamlit as st
from tabs.historia.evento10_tab import HistoriaEvento10Tab
from tabs.historia.evento11_tab import HistoriaEvento11Tab
from tabs.historia.evento12_tab import HistoriaEvento12Tab
from tabs.historia.evento1_tab import HistoriaEvento1Tab
from tabs.historia.evento2_tab import HistoriaEvento2Tab
from tabs.historia.evento3_tab import HistoriaEvento3Tab
from tabs.historia.evento4_tab import HistoriaEvento4Tab
from tabs.historia.evento5_tab import HistoriaEvento5Tab
from tabs.historia.evento6_tab import HistoriaEvento6Tab
from tabs.historia.evento7_tab import HistoriaEvento7Tab
from tabs.historia.evento8_tab import HistoriaEvento8Tab
from tabs.historia.evento9_tab import HistoriaEvento9Tab
from util.constantes import TITULO_HISTORIA, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_HISTORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_HISTORIA}]")

    # TODO: colocar grafico com todos os pontos historicos

    st.markdown('Ao longo das décadas, uma série de eventos significativos, como guerras e revoluções, moldaram o contexto geopolítico global de suas respectivas eras. Esses acontecimentos desempenharam um papel crucial na flutuação dos preços da commodity do petróleo, uma vez que é uma peça fundamental na economia mundial. A seguir, serão detalhados alguns desses eventos cruciais que influenciaram a variação de preço desse produto tão vital.')
    st.markdown('<small>Para **:blue[navegar entre as abas]**, posicione o mouse em cima das abas e segure a tecla **:blue[[SHIFT]]** e utilize botão de scroll do mouse :three_button_mouse:</small>', unsafe_allow_html=True)
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(
        tabs=[
            "Guerra do Golfo (1990-1991)",
            "Atentados terroristas nos EUA (2001)",
            "Guerra do Iraque (2003-2011)",
            "Crise financeira global (2007-2008)",
            "Primavera Árabe (2010-2012)",
            "Guerra Civil na Líbia (2011)",
            "Conflito na Síria (2011~)",
            "OPEP mantém ritmo de produção (2014)",
            "Grande produção e baixa demanda (2015)",
            "Pandemia de COVID-19 (2020-2023)",
            "Recuperação econômica pós-COVID (2021~)",
            "Conflito Rússia-Ucrânia (2022~)",
        ]
    )

    HistoriaEvento1Tab(tab0)
    HistoriaEvento2Tab(tab1)
    HistoriaEvento3Tab(tab2)
    HistoriaEvento4Tab(tab3)
    HistoriaEvento5Tab(tab4)
    HistoriaEvento6Tab(tab5)
    HistoriaEvento7Tab(tab6)
    HistoriaEvento8Tab(tab7)
    HistoriaEvento9Tab(tab8)
    HistoriaEvento10Tab(tab9)
    HistoriaEvento11Tab(tab10)
    HistoriaEvento12Tab(tab11)
