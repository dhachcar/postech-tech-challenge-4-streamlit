import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento11Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2021-02-01" and ds <= "2022-01-01"',
            query_periodo_interesse='ds >= "2021-05-01" and ds <= "2021-11-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":one::one: :blue[Recuperação econômica pós-COVID (2021~)]",
                divider="blue",
            )
            st.markdown(
                """
                A recuperação econômica em andamento pós-COVID está sendo acompanhada de mudanças no preço do petróleo, com muitos países implementando medidas para revitalizar suas economias após os impactos da pandemia. Isso inclui iniciativas de estímulo fiscal, investimentos em infraestrutura e esforços para impulsionar a demanda geral por commodities, dentre elas, o petróleo. No entanto, desafios como a desigualdade econômica persistente, a escassez de mão de obra em alguns setores e as incertezas sobre o surgimento de novas variantes do vírus continuam a influenciar os preços do petróleo e a representar obstáculos para uma recuperação completa e sustentável.
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
