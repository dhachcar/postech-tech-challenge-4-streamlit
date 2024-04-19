import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento3Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2003-01-01" and ds <= "2007-01-01"',
            query_periodo_interesse='ds >= "2003-10-01" and ds <= "2006-09-01"',
        )
        self.tab = tab
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

            st.markdown(
                """
                No gráfico a seguir...
            """
            )

            self.plot_graficos()
