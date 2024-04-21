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
                f"""
                O período de interesse (linha vermelha) analisado à seguir contempla não so a Primavera Árabe, mas eventos que se originaram também a partir dela, como a Guerra Civil da Líbia e o Conflito na Síria. Todos estes eventos em conjunto contribuem para a oscilação positiva do preço do barril de petróleo no período. De Setembro/2010 até Junho/2011 o preço variou de forma positiva em cerca de :green[{format_number(self.variacao_positiva, '%.2f')}%], tendo sua mínima em :blue[US$ {format_number(self.min, '%.2f')}] e saltando para a máxima de :blue[US$ {format_number(self.max, '%.2f')}].
            """
            )

            self.plot_graficos()
