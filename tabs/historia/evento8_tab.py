import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento8Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":eight: :blue[OPEP mantém ritmo de produção (2014)]", divider="blue"
            )
            st.markdown(
                """
                Em 2014, a Organização dos Países Exportadores de Petróleo (OPEP) decidiu manter sua produção de petróleo inalterada, apesar do excesso de oferta no mercado global. Essa decisão foi tomada principalmente para manter a participação de mercado da OPEP e pressionar os produtores de petróleo de xisto nos Estados Unidos, cuja produção havia aumentado significativamente. No entanto, essa estratégia acabou levando a uma queda drástica nos preços do petróleo, afetando profundamente a economia de muitos países dependentes do petróleo e causando instabilidade nos mercados globais de energia.
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
