import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento5Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2010-01-01" and ds <= "2012-01-01"',
            query_periodo_interesse='ds >= "2010-09-01" and ds <= "2011-06-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":five: :blue[Primavera Árabe (2010-2012)]", divider="blue")
            st.markdown(
                """
                A Primavera Árabe foi uma série de protestos e movimentos populares que eclodiram em diversos países do Oriente Médio e do Norte da África, a partir de 2010. Originados principalmente por insatisfações sociais, políticas e econômicas, esses levantes exigiam reformas políticas, democracia e direitos humanos. Iniciando na Tunísia, os protestos rapidamente se espalharam para países como Egito, Líbia, Síria, Iêmen e Bahrein, entre outros. Embora tenham gerado mudanças significativas em alguns lugares, como a queda de governos autocráticos, em outros resultaram em conflitos prolongados, guerras civis e instabilidade política, com consequências de longo prazo para toda a região.
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
