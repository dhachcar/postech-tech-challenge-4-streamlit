import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")

with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")

    st.markdown(
        """
        Após uma análise detalhada do histórico de preços do barril de petróleo, agora estamos explorando como a distribuição desses preços se desenvolve ao longo das décadas, abrangendo desde o início da série histórica estabelecida pela EIA em 1987. Além disso, examinamos indicadores como os níveis de preços mais comuns, as mínimas e máximas históricas, entre outros, os quais são apresentados e discutidos.
    """
    )

    with st.container():
        _, col, _ = st.columns([1, 8, 1])

        with col:
            fig = ff.create_distplot([df.y], group_labels=["Distribuição dos preços"])
            fig.update_layout(xaxis_title="Valor", yaxis_title="Densidade")
            fig.data[1].line.color = "red"

            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        _, col, _ = st.columns([2, 6, 2])

        with col:
            fig = go.Figure(
                layout=go.Layout(
                    xaxis=dict(title="Data"),
                    yaxis=dict(title="Preço em US$"),
                ),
            )

            fig.add_trace(
                go.Box(
                    y=df.y,
                    name="Preço do barril de petróleo Brent",
                    hoverlabel=dict(align="right"),
                )
            )

            st.plotly_chart(fig)
