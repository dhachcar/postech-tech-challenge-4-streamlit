import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento2Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":two: :blue[Atentados terroristas nos EUA (2001)]", divider="blue"
            )
            st.markdown(
                """
                O atentado de 11 de setembro de 2001 foi uma série de ataques terroristas coordenados pela organização extremista Al-Qaeda contra os Estados Unidos. Aviões comerciais foram sequestrados e deliberadamente direcionados às Torres Gêmeas do World Trade Center em Nova York, além do Pentágono em Washington, D.C. Um quarto avião caiu na Pensilvânia após os passageiros tentarem retomar o controle. Este evento resultou na perda de milhares de vidas e teve um impacto significativo na política global, segurança internacional e estratégias antiterrorismo.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2001-06-01" and ds <= "2002-01-01"'
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
