import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento1Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":one: :blue[Guerra do Golfo (1990-1991)]", divider="blue")
            st.markdown(
                """
                A Guerra do Golfo, ocorrida entre agosto de 1990 e fevereiro de 1991, foi um conflito militar que teve origem na invasão do Kuwait pelo Iraque, liderado por Saddam Hussein. A coalizão internacional liderada pelos Estados Unidos, com o apoio de países como Reino Unido, França e Arábia Saudita, interveio para expulsar as forças iraquianas do Kuwait. A guerra foi marcada por intensos combates terrestres, aéreos e navais, culminando na libertação do Kuwait e na imposição de sanções econômicas ao Iraque.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "1990-01-01" and ds <= "1991-05-01"'
            )

            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=periodo_analisado.ds,
                    y=periodo_analisado.y,
                    mode="lines",
                    name="Preço do barril de petróleo",
                )
            )

            with st.container():
                _, col1, _ = st.columns([1, 8, 1])

                with col1:
                    st.plotly_chart(fig, use_container_width=True)
