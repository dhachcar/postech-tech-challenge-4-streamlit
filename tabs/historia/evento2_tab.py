import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento2Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2001-06-01" and ds <= "2002-01-01"',
            query_periodo_interesse='ds >= "2001-09-01" and ds <= "2001-11-20"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":two: :blue[Atentados terroristas nos EUA (2001)]", divider="blue"
            )
            st.markdown(
                """
                O atentado de 11 de setembro de 2001 foi uma série de ataques terroristas coordenados pela organização extremista Al-Qaeda contra os Estados Unidos. Aviões comerciais foram sequestrados e deliberadamente direcionados às Torres Gêmeas do World Trade Center em Nova York, além do Pentágono em Washington, D.C. Um quarto avião caiu na Pensilvânia após os passageiros tentarem retomar o controle. Este evento resultou na perda de milhares de vidas e teve um impacto significativo na política global, segurança internacional e estratégias antiterrorismo.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                Analisando o gráfico na época, é possível observar uma queda abrupta no preço do barril de petróleo logo após os eventos. De forma geral, no período de interesse analisado, houve uma variação de cerca de :red[{format_number(self.variacao_negativa, '%.2f')}%], caindo de :blue[US$ {format_number(self.max, '%.2f')}] para :blue[US$ {format_number(self.min, '%.2f')}] no seu menor nível no péríodo. Vale ressaltar que nos meses seguintes, o preço continuou com tendência de baixa, oscilando para valores ainda mais baixos.
            """
            )

            self.plot_graficos()
