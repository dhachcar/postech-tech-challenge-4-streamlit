from datetime import timedelta
import time
import streamlit as st
from tabs.tab import TabInterface
import joblib
from keras.models import load_model

from util.constantes import DATA_INICIAL


class ModeloLSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.modelo = load_model("assets/modelos/lstm/lstm")
        self.scaler = joblib.load("assets/modelos/lstm/lstm-scaler.pkl")

        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Sobre do modelo]", divider="blue")

            st.markdown(
                """
                LOREM IPSUM
            """
            )

            st.subheader(":blue[Performance do modelo]", divider="blue")

            st.subheader(":blue[Executando o modelo]", divider="blue")

            with st.container():
                col, _ = st.columns([2, 6])

                with col:
                    min = DATA_INICIAL
                    max_date = DATA_INICIAL + timedelta(days=90)
                    end_date = st.date_input(
                        "Data máxima de previsão",
                        key="dt_input_lstm",
                        min_value=min,
                        max_value=max_date,
                        value=max_date,
                    )

                if st.button(":crystal_ball: Prever", key="btn_predict_lstm"):
                    with st.spinner("Processando..."):
                        time.sleep(3)

                        st.subheader(":blue[Previsão]", divider="blue")
