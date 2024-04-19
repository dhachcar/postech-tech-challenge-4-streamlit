import streamlit as st
import pandas as pd
import plotly.graph_objs as go
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


def plot_grafico_evolucao_preco_petroleo():
    def add_ponto_interesse(fig, ponto, text_index, label):
        fig.add_trace(
            go.Scatter(
                x=[ponto.ds.values[0]],
                y=[ponto.y.values[0]],
                mode="markers",
                text=1,
                marker=dict(color="red", size=10, line=dict(color="white", width=1)),
                name=label,
            )
        )
        fig.add_annotation(
            x=ponto.ds.values[0],
            y=ponto.y.values[0] + 4,
            text=text_index,
            showarrow=False,
            font=dict(color="white", size=10),
            bgcolor="red",
            borderwidth=1,
            bordercolor="white",
        )

    df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=df.ds, y=df.y, mode="lines", name="Preço do barril de petróleo")
    )
    add_ponto_interesse(
        fig, df.query('ds == "1990-08-02"'), 1, "1. Guerra do Golfo (1990-1991)"
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2001-09-11"'),
        2,
        "2. Atentados terroristas nos EUA (2001)",
    )
    add_ponto_interesse(
        fig, df.query('ds == "2003-03-20"'), 3, "3. Guerra do Iraque (2003-2011)"
    )
    add_ponto_interesse(
        fig, df.query('ds == "2007-08-01"'), 4, "4. Crise financeira global (2007-2008)"
    )
    add_ponto_interesse(
        fig, df.query('ds == "2010-12-20"'), 5, "5. Primavera Árabe (2010-2012)"
    )
    add_ponto_interesse(
        fig, df.query('ds == "2011-02-17"'), 6, "6. Guerra Civil na Líbia (2011)"
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2011-03-15"'),
        7,
        "7. Conflito na Síria (a partir de 2011)",
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2014-11-28"'),
        8,
        "8. OPEP mantém ritmo de produção (2014)",
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2015-01-02"'),
        9,
        "9. Grande produção e baixa demanda (2015)",
    )
    add_ponto_interesse(
        fig, df.query('ds == "2020-01-30"'), 10, "10. Pandemia de COVID-19 (2020-2023)"
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2021-07-01"'),
        11,
        "11. Recuperação econômica pós-COVID (2021-presente)",
    )
    add_ponto_interesse(
        fig,
        df.query('ds == "2022-02-24"'),
        12,
        "12. Conflito Rússia-Ucrânia (2022-presente)",
    )

    fig.add_annotation(
        x=0.5,
        y=-0.15,
        xref="paper",
        yref="paper",
        text="<b>Fonte: EIA, 2024</b>",
        showarrow=False,
        font=dict(color="black", size=10),
        bgcolor="white",
        borderwidth=1,
        bordercolor="black",
    )

    fig.update_layout(
        title="Evolução do preço do barril de petróleo Brent ao longo das decádas (1987 até hoje)",
        xaxis_title="Data",
        yaxis_title="Preço em US$",
        height=640,
    )

    st.plotly_chart(fig, use_container_width=True)


with st.container():
    # css específico da página
    with open("assets/css/historia.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.header(f":orange[{TITULO_HISTORIA}]")
    st.markdown(
        """
        Ao longo das décadas, uma série de eventos significativos, como guerras e revoluções, moldaram o contexto geopolítico global de suas respectivas eras. Esses acontecimentos desempenharam um papel crucial na flutuação dos preços da commodity do petróleo, uma vez que é uma peça fundamental na economia mundial.\n
        A seguir, serão detalhados 12 desses eventos cruciais, ordenados de forma cronológica, conforme a seguir:
        * Guerra do Golfo (1990-1991)
        * Atentados terroristas nos EUA (2001)
        * Guerra do Iraque (2003-2011)
        * Crise financeira global (2007-2008)
        * Primavera Árabe (2010-2012)
        * Guerra Civil na Líbia (2011)
        * Conflito na Síria (2011~)
        * OPEP mantém ritmo de produção (2014)
        * Grande produção e baixa demanda (2015)
        * Pandemia de COVID-19 (2020-2023)
        * Recuperação econômica pós-COVID (2021~)
        * Conflito Rússia-Ucrânia (2022~)
    """
    )

    plot_grafico_evolucao_preco_petroleo()

    st.markdown(
        "<small>Para **:blue[navegar entre as abas]**, posicione o mouse em cima das abas e segure a tecla **:blue[[SHIFT]]** e utilize botão central de scroll do mouse :three_button_mouse:</small>",
        unsafe_allow_html=True,
    )
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(
        tabs=[
            ":one: Guerra do Golfo (1990-1991)",
            ":two: Atentados terroristas nos EUA (2001)",
            ":three: Guerra do Iraque (2003-2011)",
            ":four: Crise financeira global (2007-2008)",
            ":five: Primavera Árabe (2010-2012)",
            ":six: Guerra Civil na Líbia (2011)",
            ":seven: Conflito na Síria (2011~)",
            ":eight: OPEP mantém ritmo de produção (2014)",
            ":nine: Grande produção e baixa demanda (2015)",
            ":one::zero: Pandemia de COVID-19 (2020-2023)",
            ":one::one: Recuperação econômica pós-COVID (2021~)",
            ":one::two: Conflito Rússia-Ucrânia (2022~)",
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
