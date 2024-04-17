import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento9Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":nine: :blue[Grande produção e baixa demanda (2015)]", divider="blue"
            )
            st.markdown(
                """
                Em 2015, houve uma situação de grande produção de petróleo em meio a uma baixa demanda global. Isso foi resultado da decisão da Organização dos Países Exportadores de Petróleo (OPEP) de manter a produção, combinada com um enfraquecimento da demanda devido a desacelerações econômicas em várias partes do mundo. O excesso de oferta de petróleo levou a uma queda acentuada nos preços do petróleo bruto, o que afetou severamente as economias dos países produtores de petróleo e provocou uma reestruturação significativa no setor de energia em escala global.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2014-01-01" and ds <= "2016-06-01"'
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
