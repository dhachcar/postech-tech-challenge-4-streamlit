from datetime import timedelta
import time
import numpy as np
import pandas as pd
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

        self.render()

    '''
    def lstm_predict(num_prediction, series, modelo):
        look_back = 5
        prediction_list = series[-look_back:]

        for _ in range(num_prediction):
            x = prediction_list[-look_back:]
            x = x.reshape((1, look_back, 1))
            out = modelo.predict(x)[0][0]
            prediction_list = np.append(prediction_list, out)

        prediction_list = prediction_list[look_back - 1:]

        return prediction_list

    def lstm_predict_dates(datas, num_prediction):
        last_date = datas.values[-1]
        prediction_dates = pd.date_range(last_date, periods=num_prediction + 1).tolist()

        return prediction_dates
    '''

    def predict(self, min, end_date):
        date_difference = min - end_date
        days_between = np.abs(date_difference.days)

        # generate the input and output sequences
        # TODO: testar esse lookback, se ele muda, quebra o codigo
        n_lookback = 10  # length of input sequences (lookback period)
        n_forecast = days_between  # length of output sequences (forecast period)

        y = self.df["y"]
        y = y.values.reshape(-1, 1)

        X = []
        Y = []

        for i in range(n_lookback, len(y) - n_forecast + 1):
            X.append(y[i - n_lookback : i])
            Y.append(y[i : i + n_forecast])

        X = np.array(X)
        Y = np.array(Y)

        # generate the forecasts
        X_ = y[-n_lookback:]  # last available input sequence
        X_ = X_.reshape(1, n_lookback, 1)

        st.write(X_)



        # TODO: atualizar os itens de lookback para ele olhar e adicionar no df

        Y_append = []
        for i in range(0, n_forecast):
            Y_ = self.modelo.predict(X_).reshape(-1, 1)
            Y_ = self.scaler.inverse_transform(Y_)
            Y_append.append(Y_)



        st.write(Y_append)

        # organize the results in a data frame
        df_past = self.df.copy()
        df_past.rename(columns={"ds": "Date", "y": "Actual"}, inplace=True)
        df_past["Date"] = pd.to_datetime(df_past["Date"])
        df_past["Forecast"] = np.nan
        df_past["Forecast"].iloc[-1] = df_past["Actual"].iloc[-1]

        df_future = pd.DataFrame(columns=["Date", "Actual", "Forecast"])
        df_future["Date"] = pd.date_range(
            start=df_past["Date"].iloc[-1] + pd.Timedelta(days=1), periods=n_forecast
        )
        df_future["Forecast"] = Y_append
        df_future["Actual"] = np.nan

        results = pd.concat([df_past, df_future], ignore_index=True).set_index("Date")

        st.dataframe(results)

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
