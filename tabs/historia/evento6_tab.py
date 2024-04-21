import streamlit as st
from tabs.historia.evento_tab import EventoTab
from util.layout import format_number


class HistoriaEvento6Tab(EventoTab):
    def __init__(self, tab):
        super().__init__(
            query_periodo_analisado='ds >= "2010-01-01" and ds <= "2012-01-01"',
            query_periodo_interesse='ds >= "2010-09-01" and ds <= "2011-06-01"',
        )
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":six: :blue[Guerra Civil na Líbia (2011)]", divider="blue")
            st.markdown(
                """
                A guerra civil da Líbia foi um conflito que eclodiu em 2011, como parte dos movimentos da Primavera Árabe, levando à queda do regime autocrático de Muammar Gaddafi. No entanto, após a deposição de Gaddafi, o país mergulhou em um período de turbulência e instabilidade política, com grupos armados rivais competindo pelo controle do território e dos recursos. A disputa entre as diferentes facções levou a uma guerra civil prolongada, marcada por violência generalizada, violações dos direitos humanos e intervenções estrangeiras. Essa situação resultou em um cenário de fragmentação política e divisão territorial, com o país dividido entre governos rivais e grupos armados, contribuindo para um estado de caos e incerteza que persiste até os dias de hoje.
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
