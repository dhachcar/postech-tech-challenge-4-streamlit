import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento10Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2020-01-01" and ds <= "2021-01-01"',
            query_periodo_interesse='ds >= "2020-02-01" and ds <= "2020-05-01"',
        )
        self.tab = tab
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

            st.markdown(
                """
                No gráfico a seguir...
            """
            )

            self.plot_graficos()
