import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento1Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "1990-01-01" and ds <= "1991-05-01"',
            query_periodo_interesse='ds >= "1990-07-22" and ds <= "1991-01-31"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":one: :blue[Guerra do Golfo (1990-1991)]", divider="blue")
            st.markdown(
                """
                A Guerra do Golfo, ocorrida entre agosto de 1990 e fevereiro de 1991, foi um conflito militar que teve origem na invasão do Kuwait pelo Iraque, liderado por Saddam Hussein. A coalizão internacional liderada pelos Estados Unidos, com o apoio de países como Reino Unido, França e Arábia Saudita, interveio para expulsar as forças iraquianas do Kuwait. A guerra foi marcada por intensos combates terrestres, aéreos e navais, culminando na libertação do Kuwait e na imposição de sanções econômicas ao Iraque.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                No gráfico a seguir, analisamos exclusivamente as datas mais próximas e relevantes ao evento estudado e tomando como exemplo o período de :blue[07/02/1990] até :blue[31/01/1991], pode-se observar que no seu auge, o preço do petróleo mais que dobrou, em cerca de :green[{format_number(self.variacao_positiva, '%.2f')}%], indo de :blue[US$ {format_number(self.min, '%.2f')}] para cerca de :blue[US$ {format_number(self.max, '%.2f')}].\n
                A partir de fevereiro de 1991, o preço voltou a patamares semelhantes à antes do início da Guerra do Golfo.
            """
            )

            self.plot_graficos()
