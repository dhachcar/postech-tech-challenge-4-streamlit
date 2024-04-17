import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento5Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":five: :blue[Primavera Árabe (2010-2012)]", divider="blue")
            st.markdown(
                """
                A Primavera Árabe foi uma série de protestos e movimentos populares que eclodiram em diversos países do Oriente Médio e do Norte da África, a partir de 2010. Originados principalmente por insatisfações sociais, políticas e econômicas, esses levantes exigiam reformas políticas, democracia e direitos humanos. Iniciando na Tunísia, os protestos rapidamente se espalharam para países como Egito, Líbia, Síria, Iêmen e Bahrein, entre outros. Embora tenham gerado mudanças significativas em alguns lugares, como a queda de governos autocráticos, em outros resultaram em conflitos prolongados, guerras civis e instabilidade política, com consequências de longo prazo para toda a região.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2010-01-01" and ds <= "2012-01-01"'
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
