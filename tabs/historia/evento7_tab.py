import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento7Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2010-01-01" and ds <= "2012-01-01"',
            query_periodo_interesse='ds >= "2010-09-01" and ds <= "2011-06-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":seven: :blue[Conflito na Síria (2011~)]", divider="blue")
            st.markdown(
                """
                O conflito na Síria, em curso desde 2011, é uma crise humanitária devastadora que já deixou milhões de pessoas deslocadas e causou uma terrível perda de vidas. Originado de protestos pacíficos contra o governo, o conflito rapidamente se transformou em uma guerra civil complexa, envolvendo múltiplas facções, incluindo o governo sírio, rebeldes, grupos extremistas e intervenções estrangeiras. Bombardeios, ataques aéreos e cercos a áreas civis têm sido comuns, causando um sofrimento indescritível para a população síria, com acesso limitado a alimentos, água e cuidados médicos. Apesar de esforços diplomáticos e tréguas temporárias, a resolução do conflito parece distante
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
