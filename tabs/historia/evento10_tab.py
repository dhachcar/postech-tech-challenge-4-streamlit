import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento10Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":one::zero: :blue[Pandemia de COVID-19 (2020-2023)]", divider="blue"
            )
            st.markdown(
                """
                A pandemia de COVID-19, causada pelo coronavírus SARS-CoV-2, emergiu em dezembro de 2019 na cidade de Wuhan, na China, e rapidamente se disseminou pelo mundo, sendo declarada uma pandemia pela Organização Mundial da Saúde em março de 2020. O vírus se espalhou de forma exponencial, resultando em milhões de casos confirmados e mortes em todos os continentes. As medidas para conter a propagação, como lockdowns, distanciamento social e uso de máscaras, causaram impactos econômicos, sociais e psicológicos significativos, evidenciando fragilidades nos sistemas de saúde e destacando desigualdades socioeconômicas.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2020-01-01" and ds <= "2021-01-01"'
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
