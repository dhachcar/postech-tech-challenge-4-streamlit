import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento12Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":one::two: :blue[Conflito Rússia-Ucrânia (2022~)]", divider="blue"
            )
            st.markdown(
                """
                A escalada do conflito entre a Ucrânia e a Rússia, iniciada em fevereiro de 2022, foi caracterizada por uma intensificação das tensões na região leste da Ucrânia, especialmente nas áreas controladas por separatistas pró-Rússia em Donetsk e Lugansk. Os confrontos diretos entre as forças ucranianas e as tropas russas resultaram em relatos de mortes e um aumento significativo nos preços do gás e do petróleo, ampliando as preocupações sobre os impactos econômicos e geopolíticos da crise.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2022-01-01" and ds <= "2023-01-01"'
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
