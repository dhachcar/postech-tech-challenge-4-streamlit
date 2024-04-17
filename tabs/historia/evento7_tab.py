import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento7Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":seven: :blue[Conflito na Síria (2011~)]", divider="blue")
            st.markdown(
                """
                O conflito na Síria, em curso desde 2011, é uma crise humanitária devastadora que já deixou milhões de pessoas deslocadas e causou uma terrível perda de vidas. Originado de protestos pacíficos contra o governo, o conflito rapidamente se transformou em uma guerra civil complexa, envolvendo múltiplas facções, incluindo o governo sírio, rebeldes, grupos extremistas e intervenções estrangeiras. Bombardeios, ataques aéreos e cercos a áreas civis têm sido comuns, causando um sofrimento indescritível para a população síria, com acesso limitado a alimentos, água e cuidados médicos. Apesar de esforços diplomáticos e tréguas temporárias, a resolução do conflito parece distante
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
