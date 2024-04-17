import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento4Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":four: :blue[Crise financeira global (2007-2008)]", divider="blue"
            )
            st.markdown(
                """
                A crise financeira de 2007-2008, conhecida como a Grande Recessão, teve seu início na instabilidade do mercado imobiliário dos Estados Unidos. O problema surgiu com a concessão generalizada de empréstimos hipotecários de alto risco, muitas vezes para indivíduos sem capacidade financeira para quitá-los. Esses empréstimos foram então transformados em produtos financeiros complexos e comercializados internacionalmente. Com a queda do mercado imobiliário e a desvalorização dos imóveis, muitos mutuários enfrentaram dificuldades para honrar suas hipotecas, resultando em um aumento significativo da inadimplência. Esse efeito em cascata afetou grandes instituições financeiras, desencadeando uma crise que se propagou globalmente, resultando em recessão, alto desemprego e deixando marcas profundas nas economias e na política ao redor do mundo.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            periodo_analisado = self.df.query(
                'ds >= "2007-01-01" and ds <= "2009-08-01"'
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
