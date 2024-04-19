import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento9Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2014-01-01" and ds <= "2016-06-01"',
            query_periodo_interesse='ds >= "2014-07-01" and ds <= "2015-05-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":nine: :blue[Grande produção e baixa demanda (2015)]", divider="blue"
            )
            st.markdown(
                """
                Em 2015, houve uma situação de grande produção de petróleo em meio a uma baixa demanda global. Isso foi resultado da decisão da Organização dos Países Exportadores de Petróleo (OPEP) de manter a produção, combinada com um enfraquecimento da demanda devido a desacelerações econômicas em várias partes do mundo. O excesso de oferta de petróleo levou a uma queda acentuada nos preços do petróleo bruto, o que afetou severamente as economias dos países produtores de petróleo e provocou uma reestruturação significativa no setor de energia em escala global.
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
