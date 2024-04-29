from datetime import timedelta
import time
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import streamlit as st
from tabs.tab import TabInterface
import joblib
from keras.models import load_model

from util.constantes import DATA_INICIAL


class ModeloLSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.modelo = load_model("assets/modelos/lstm/lstm")
        self.scaler = joblib.load("assets/modelos/lstm/lstm-scaler.pkl")

        self.df = self.df.sort_values(by="ds", ascending=True)

        self.render()

    def predict(self, min, end_date):
        date_difference = min - end_date
        days_between = np.abs(date_difference.days)

        # generate the input and output sequences
        # TODO: testar esse lookback, se ele muda, quebra o codigo
        n_lookback = 10  # length of input sequences (lookback period), o mesmo utilizado para treinamento TODO: colocar isso no texto
        n_forecast = days_between  # length of output sequences (forecast period)

        y_scaled = self.scaler.transform(self.df["y"].values.reshape(-1, 1))
        prediction_list = y_scaled[-n_lookback:]

        for _ in range(1, n_forecast):
            x = prediction_list[-n_lookback:]
            x = x.reshape(1, n_lookback, 1)
            out = self.modelo.predict(x).reshape(-1, 1)
            prediction_list = np.append(prediction_list, out)

        prediction_list = prediction_list[n_lookback - 1 :]

        # df passado
        df_past = self.df.copy()
        df_past.rename(columns={"y": "valor_real"}, inplace=True)
        df_past["ds"] = pd.to_datetime(df_past["ds"])
        df_past["valor_real"] = df_past["valor_real"].values.reshape(-1, 1)
        df_past["previsao"] = np.nan
        df_past["previsao"].iloc[-1] = df_past["valor_real"].iloc[-1]

        # df futuro
        df_future = pd.DataFrame(columns=["ds", "valor_real", "previsao"])
        df_future["ds"] = pd.date_range(
            pd.to_datetime(self.df["ds"]).max() + timedelta(days=1), periods=n_forecast
        ).tolist()
        df_future["valor_real"] = np.nan
        df_future["previsao"] = self.scaler.inverse_transform(
            prediction_list.reshape(-1, 1)
        )

        # concat_results = pd.concat([df_past, df_future], ignore_index=True).set_index("ds")

        # plot
        results_past = df_past
        results_past = results_past.set_index("ds")

        fig = go.Figure(layout=go.Layout(title="Forecast IBOVESPA"))
        fig.add_trace(
            go.Scatter(
                x=results_past.index, y=results_past["valor_real"], name="Atual"
            ),
        )
        fig.add_trace(
            go.Scatter(
                x=df_future["ds"],
                y=df_future["previsao"],
                name="Previsão",
                mode="lines",
                line=dict(color="red", width=2),
            ),
        )

        st.plotly_chart(fig)

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

                        self.predict(min, end_date)

                        st.success("Processamento concluído! :white_check_mark:")
