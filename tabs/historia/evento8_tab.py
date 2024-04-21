import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento8Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2014-01-01" and ds <= "2016-06-01"',
            query_periodo_interesse='ds >= "2014-06-01" and ds <= "2015-05-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":eight: :blue[OPEP mantém ritmo de produção (2014)]", divider="blue"
            )
            st.markdown(
                """
                Em 2014, a Organização dos Países Exportadores de Petróleo (OPEP) decidiu manter sua produção de petróleo inalterada, apesar do excesso de oferta no mercado global. Essa decisão foi tomada principalmente para manter a participação de mercado da OPEP e pressionar os produtores de petróleo de xisto nos Estados Unidos, cuja produção havia aumentado significativamente. No entanto, essa estratégia acabou levando a uma queda drástica nos preços do petróleo, afetando profundamente a economia de muitos países dependentes do petróleo e causando instabilidade nos mercados globais de energia.
            """
            )

            st.subheader(
                ":chart: :blue[Analisando a variação de preço no período]",
                divider="blue",
            )

            st.markdown(
                f"""
                O próximo período de interesse analisado se encontra entre Julho/2014 e Abril/2015.  Foi uma época na qual a produção de petróleo estava em alta mas a demanda em queda. Como todos sabemos, o mercado é regido pela lei da oferta e demanda e portanto, quando há muito de um produto disponível no mercado mas pouca demanda por ele, seu preço sofrerá uma desvalorização acentuada. É exatamente este movimento que podemos observar no período em questão. Após atingir uma máxima de :blue[US$ {format_number(self.max, '%.2f')}], o preço do barril chegou a cair para a mínima de :blue[US$ {format_number(self.min, '%.2f')}] no período, o que representa uma variação de :red[{format_number(self.variacao_negativa, '%.2f')}%] no preço. Observando os períodos posteriores ao analisado, ainda é possível visualizar novas oscilações negativas, atingindo valores ainda mais baixos.
            """
            )

            self.plot_graficos()
