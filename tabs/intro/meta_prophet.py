import streamlit as st
from tabs.tab import TabInterface


class IntroMetaProphet(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Meta Prophet]", divider="blue"
            )
            st.markdown(
                """
                Segundo a página do projeto, o Prophet é uma ferranebta para previsão de dados de séries temporais com base em um modelo aditivo onde tendências não lineares são ajustadas com sazonalidades anuais, semanais e diárias, além de efeitos de feriados. Ele funciona melhor com séries temporais que possuem fortes efeitos sazonais e vários anos de dados históricos. O Prophet é robusto em relação a dados ausentes e mudanças na tendência e geralmente lida bem com valores discrepantes.\n\n
                Além disso ele é um software de código aberto, disponível no GitHub e mantido pela equipe de cientistas de dados da Meta.
                <br/><br/>
            """,
                unsafe_allow_html=True,
            )

            with st.container():
                _, col0, _ = st.columns([4, 2, 4])

                with col0:
                    st.image(
                        "assets/imgs/logo-meta-prophet.svg", width=220, caption="Logo do Meta Prophet"
                    )
