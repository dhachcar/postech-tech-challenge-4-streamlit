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
                f"""
                O período de interesse (linha vermelha) analisado à seguir contempla não so a Primavera Árabe, mas eventos que se originaram também a partir dela, como a Guerra Civil da Líbia e o Conflito na Síria. Todos estes eventos em conjunto contribuem para a oscilação positiva do preço do barril de petróleo no período. De Setembro/2010 até Junho/2011 o preço variou de forma positiva em cerca de :green[{format_number(self.variacao_positiva, '%.2f')}%], tendo sua mínima em :blue[US$ {format_number(self.min, '%.2f')}] e saltando para a máxima de :blue[US$ {format_number(self.max, '%.2f')}].
            """
            )

            self.plot_graficos()
