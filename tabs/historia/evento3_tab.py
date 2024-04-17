import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento3Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":three: :blue[Guerra do Iraque (2003-2011)]", divider="blue")
            st.markdown(
                """
                A Guerra do Iraque, também conhecida como Guerra do Golfo II, começou em março de 2003 quando uma coalizão liderada pelos Estados Unidos invadiu o país. O objetivo principal era remover Saddam Hussein do poder, alegando que ele possuía armas de destruição em massa e apoiava o terrorismo. Depois que o regime de Hussein foi derrubado, o conflito evoluiu para uma longa e complexa guerra de guerrilha, que resultou em muitas vidas perdidas e deixou um legado de instabilidade na região do Oriente Médio.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2003-01-01" and ds <= "2007-01-01"'
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
