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
from util.layout import format_number


class ModeloLSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")
        self.modelo = load_model("assets/modelos/lstm/lstm")
        self.scaler = joblib.load("assets/modelos/lstm/lstm-scaler.pkl")
        self.df_performance = pd.read_csv("assets/csv/lstm-performance.csv")

        self.df = self.df.sort_values(by="ds", ascending=True)
        self.df_performance.set_index("indicador", inplace=True)

        self.render()

    def predict(self, min, end_date):
        date_difference = min - end_date
        days_between = np.abs(date_difference.days)

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

        with st.container():
            clone = df_future.copy()
            clone["ds"] = clone["ds"].apply(
                lambda x: pd.to_datetime(x).strftime("%d/%m/%Y")
            )
            clone.rename(columns={"ds": "Data", "previsao": "Preço"}, inplace=True)

            _, col, _ = st.columns([3, 4, 3])

            with col:
                st.dataframe(
                    clone[["Data", "Preço"]],
                    use_container_width=True,
                    hide_index=True,
                )

        with st.container():
            self.plot_grafico_previsao(df_past, df_future, n_forecast)

    def plot_grafico_previsao(self, df_past, df_future, total_dias_previsao):
        # plot
        results_past = df_past.query('ds >= "2020-01-01"')
        results_past = results_past.set_index("ds")

        fig = go.Figure(
            layout=go.Layout(
                title=f"Distribuição do valor (US$) do barril de petróleo Brent entre 2020 e os dias atuais + previsão dos próximos {total_dias_previsao} dia(s)",
                showlegend=True,
                margin=dict(t=150),
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
                ),
            )
        )
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

        st.plotly_chart(fig, use_container_width=True)

    def render(self):
        with self.tab:
            st.subheader(":blue[Sobre do modelo]", divider="blue")

            st.markdown(
                """
                Este modelo foi criado com com base no :blue[Tensorflow & Keras] e também considerou os dados históricos do preço do barril de petróleo Brent a partir de :blue[01/01/2020]. Vale notar que o período de lookback treinado no LSTM foi de 10 dias, o que significa que para realizar suas previsoões, ele sempre irá utilizar os valores dos últimos 10 dias.
            """
            )

            st.subheader(":blue[Performance do modelo]", divider="blue")

            mse = format_number(self.df_performance.loc["MSE"], "%0.8f")
            rmse = format_number(self.df_performance.loc["RMSE"], "%0.8f")
            mape = format_number(self.df_performance.loc["MAPE"], "%0.8f")

            st.markdown(
                f"""
                Nesta seção, apresentamos alguns indicadores de erro calculados para o modelo LSTM. O MSE é de :blue[{mse}], indicando a média dos quadrados das diferenças entre os valores previstos e os valores reais, sugerindo um bom ajuste do modelo aos dados. O RMSE, derivado do MSE, é de cerca de :blue[{rmse}], representando a raiz quadrada do MSE, oferecendo uma medida do erro médio do modelo em relação aos valores reais. Já o MAPE possui o valor de :blue[{mape}], que é a média dos percentuais absolutos de erro em relação aos valores reais, fornecendo uma medida de precisão relativa em termos percentuais. Todos esses valores indicam uma boa performance do modelo de previsão.
            """
            )

            with st.container():
                _, col0, col1, col2, _ = st.columns([1, 1, 1, 1, 1])

                with col0:
                    st.metric(
                        label="MSE",
                        value=mse,
                    )

                with col1:
                    st.metric(
                        label="RMSE",
                        value=rmse,
                    )

                with col2:
                    st.metric(
                        label="MAPE",
                        value=mape,
                    )

            st.subheader(":blue[Executando o modelo]", divider="blue")

            st.markdown(
                f"""
                Nesta seção, é possível escolher uma data no futuro e o modelo irá prever o preço do barril de petróleo até a data escolhida. Devido aos indicadores de erro tenderem a aumentar de forma exponencial quanto maior o tempo no futuro, limitamos o horizonte máximo em 90 dias a partir da data base :blue[{DATA_INICIAL.strftime("%d/%m/%Y")}].
            """
            )

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

                        st.markdown(
                            f"**:orange[IMPORTANTE:] a previsão é feita com a data base em :blue[{DATA_INICIAL.strftime('%d/%m/%Y')}] (último preço do barril de petróleo coletado).**"
                        )

                        self.predict(min, end_date)

                        st.success("Processamento concluído! :white_check_mark:")
