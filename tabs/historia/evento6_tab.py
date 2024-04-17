import streamlit as st
from tabs.tab import TabInterface
import pandas as pd
import plotly.graph_objs as go


class HistoriaEvento6Tab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":six: :blue[Guerra Civil na Líbia (2011)]", divider="blue")
            st.markdown(
                """
                A guerra civil da Líbia foi um conflito que eclodiu em 2011, como parte dos movimentos da Primavera Árabe, levando à queda do regime autocrático de Muammar Gaddafi. No entanto, após a deposição de Gaddafi, o país mergulhou em um período de turbulência e instabilidade política, com grupos armados rivais competindo pelo controle do território e dos recursos. A disputa entre as diferentes facções levou a uma guerra civil prolongada, marcada por violência generalizada, violações dos direitos humanos e intervenções estrangeiras. Essa situação resultou em um cenário de fragmentação política e divisão territorial, com o país dividido entre governos rivais e grupos armados, contribuindo para um estado de caos e incerteza que persiste até os dias de hoje.
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
