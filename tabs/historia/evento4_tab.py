import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento4Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2007-01-01" and ds <= "2009-08-01"',
            query_periodo_interesse='ds >= "2008-05-01" and ds <= "2009-02-01"',
        )
        self.tab = tab
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

            st.markdown(
                """
                No gráfico a seguir...
            """
            )

            self.plot_graficos()
