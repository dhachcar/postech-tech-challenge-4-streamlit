import streamlit as st
from tabs.tab import TabInterface


class IntroTensorflowKerasLSTM(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Tensorflow]", divider="blue")
            st.markdown(
                """
                    TensorFlow é uma plataforma de código aberto para aprendizado de máquina desenvolvida pelo Google. Ele oferece uma estrutura flexível e abrangente para construir e treinar modelos de aprendizado de máquina, utilizando tensores como sua estrutura básica de dados. TensorFlow é altamente escalável e adequado para uma ampla gama de aplicativos de aprendizado de máquina, desde reconhecimento de imagem até processamento de linguagem natural.
                """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Keras]", divider="blue")

            st.markdown(
                """
                Keras, por outro lado, é uma biblioteca de código aberto escrita em Python que fornece uma interface de alto nível para construir e treinar modelos de aprendizado profundo. Ele é projetado para ser simples, modular e extensível, permitindo que os desenvolvedores construam rapidamente protótipos de modelos de rede neural. Keras atua como uma camada de abstração sobre diferentes frameworks de aprendizado profundo, incluindo TensorFlow, facilitando o processo de desenvolvimento de modelos.
            """
            )

            st.subheader(":blue[Relação entre ambos]", divider="blue")

            st.markdown(
                """
                O TensorFlow e o Keras estão relacionados de tal forma que, o Keras é integrado ao TensorFlow como sua API de alto nível padrão a partir da versão 2.0. Isso significa que os usuários da biblioteca podem aproveitar a simplicidade e flexibilidade do Keras enquanto se beneficiam da escalabilidade e desempenho do TensorFlow como backend. Essa integração torna mais fácil para os desenvolvedores construir, treinar e implantar modelos de aprendizado profundo usando TensorFlow com a simplicidade e a conveniência do Keras.
            """
            )

            st.subheader(":blue[LSTM]", divider="blue")

            st.markdown(
                """
                O LSTM (Long Short-Term Memory) é um tipo especial de rede neural usada para entender padrões em sequências de dados, como textos ou séries temporais. Ela é capaz de lembrar informações importantes por mais tempo, o que a torna eficaz em tarefas como tradução de idiomas e previsão do tempo.
            """
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])

                with col0:
                    st.image(
                        "assets/imgs/logo-tensorflow.png",
                        width=256,
                        caption="Logo do Tensorflow",
                    )

                with col1:
                    st.image(
                        "assets/imgs/logo-keras.png", width=256, caption="Logo do Keras"
                    )
