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
                f"""
                Com a vacinação em massa e a diminuição de casos e mortes de COVID-19 na metade do ano, o mundo começou a se recuperar dos efeitos da pandemia de forma tímida. Apesar de tudo, naquele momento a pandemia ainda estava em curso, mas o choque inicial e as ondas mais severas já haviam passado. Essa recuperação tímida pode ser observada no gráfico abaixo, onde o menor valor atingido foi de :blue[US$ {format_number(self.min, '%.2f')}] e o maior valor foi de :blue[US$ {format_number(self.max, '%.2f')}], uma variação positiva de :green[{format_number(self.variacao_positiva, '%.2f')}%]. Vale notar que ainda hoje, em pleno 2024, a recuperação econômica continua em andamento e ainda sentimos os efeitos da pandemia. Muito provavelmente, eles ainda serão sentidos pelos próximos anos.
            """
            )

            self.plot_graficos()
