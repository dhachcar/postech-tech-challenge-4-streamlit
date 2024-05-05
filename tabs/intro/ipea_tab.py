import streamlit as st
from tabs.tab import TabInterface


class IntroIPEATab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Instituto de Pesquisa Econômica Aplicada (IPEA)]", divider="blue"
            )
            st.markdown(
                """
                O Instituto de Pesquisa Econômica Aplicada (IPEA) é uma instituição governamental brasileira vinculada ao Ministério da Economia, responsável por produzir pesquisas e estudos de alta qualidade em economia e políticas públicas. Fundado em 1964, o IPEA desempenha um papel fundamental na formulação e avaliação de políticas governamentais, fornecendo análises e recomendações baseadas em evidências para contribuir com o desenvolvimento socioeconômico do Brasil.\n\n
                Sua produção de conhecimento abrange uma ampla gama de áreas, incluindo macroeconomia, mercado de trabalho, saúde, educação, meio ambiente e segurança pública, entre outras, e sua atuação é reconhecida nacional e internacionalmente como uma fonte confiável de informações e análises para tomadores de decisão, acadêmicos e sociedade em geral.\n\n
                Neste projeto, inicialmente foram consultados os dados do IPEA, mas no fim, a base final foi obtida diretamente da mesma fonte que eles utilizam, o EIA.
                <br/><br/>
            """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _ = st.columns([4, 2, 4])

                with col0:
                    st.image(
                        "assets/imgs/logo-ipea.png", width=128, caption="Logo do IPEA"
                    )
