import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento12Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2022-01-01" and ds <= "2023-01-01"',
            query_periodo_interesse='ds >= "2022-02-01" and ds <= "2022-04-01"',
        )
        self.tab = tab
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

            st.markdown(
                """
                No gráfico a seguir...
            """
            )

            self.plot_graficos()
