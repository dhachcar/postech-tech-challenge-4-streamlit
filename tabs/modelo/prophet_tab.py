import streamlit as st
from tabs.tab import TabInterface
from datetime import timedelta
import time
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from prophet.plot import plot_plotly
from prophet.serialize import model_from_json

from util.constantes import DATA_INICIAL
from util.layout import format_number


class ModeloProphetTab(TabInterface):
    df_performance: pd.DataFrame
    df_previsao: pd.DataFrame
    modelo = None

    def __init__(self, tab):
        self.tab = tab

        # carrega o csv de performance
        self.df_performance = pd.read_csv("assets/csv/prophet-performance.csv")
        self.df_performance["data_no_futuro"] = pd.to_datetime(
            self.df_performance["data_no_futuro"]
        )

        # carrega o modelo prophet
        with open("assets/modelos/prophet/prophet-model.json", "r") as f_in:
            self.modelo = model_from_json(f_in.read())

        self.render()

    def plot_grafico_performance(self):
        fig = go.Figure(layout=go.Layout(yaxis=dict(type="log")))
        fig.add_trace(
            go.Scatter(
                x=self.df_performance["data_no_futuro"],
                y=self.df_performance["mse"],
                mode="lines",
                name="MSE",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=self.df_performance["data_no_futuro"],
                y=self.df_performance["rmse"],
                mode="lines",
                name="RMSE",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=self.df_performance["data_no_futuro"],
                y=self.df_performance["mae"],
                mode="lines",
                name="MAE",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=self.df_performance["data_no_futuro"],
                y=self.df_performance["mape"],
                mode="lines",
                name="MAPE",
            )
        )

        st.markdown(
            """
            TODO: rever este texto... O gráfico teve seu eixo Y escalonado com log10, para permitir uma visualização mais apurada do aumento dos indicadores de erro no decorrer do tempo, quanto maior o intervalo.
        """
        )
        st.plotly_chart(fig)

    def plot_grafico_previsao(self):
        # gráfico do plotly
        fig = plot_plotly(
            self.modelo, self.df_previsao, trend=True, figsize=(1200, 900)
        )

        # objetos de linha
        linha_azul = go.Scatter(
            x=[2020, self.df_previsao.iloc[-1, :].ds],
            y=[0, 0],
            mode="lines",
            line=dict(color="blue"),
            name="US$ 0,00",
        )
        linha_amarela = go.Scatter(
            x=[2020, self.df_previsao.iloc[-1, :].ds],
            y=[50, 50],
            mode="lines",
            line=dict(color="green"),
            name="US$ 50,00",
        )
        linha_vermelha = go.Scatter(
            x=[2020, self.df_previsao.iloc[-1, :].ds],
            y=[100, 100],
            mode="lines",
            line=dict(color="red"),
            name="US$ 100,00",
        )

        # dados gerais do gráfico
        fig.update_layout(
            title="Distribuição do valor (US$) do barril de petróleo Brent entre 2020 e os dias atuais + previsão dos próximos 30 dias",
            showlegend=True,
        )
        fig.update_traces(marker=dict(color="darkorange"))

        # atualizando legendas
        fig.data[0].name = "Realidade"
        fig.data[1].name = "Banda inferior da previsão"
        fig.data[1].fill = "tonexty"
        fig.data[1].fillcolor = "rgba(0, 114, 178, 0.2)"
        fig.data[2].name = "Previsão"
        fig.data[3].name = "Banda superior da previsão"
        fig.data[4].name = "Tendência"

        # adiciona as linhas
        fig.add_trace(linha_azul)
        fig.add_trace(linha_amarela)
        fig.add_trace(linha_vermelha)

        st.plotly_chart(fig)

    def render(self):
        with self.tab:
            st.write("teste1")

            st.markdown("Dados base em 08/04/2024")
            st.dataframe(self.df_performance)

            metrica_primeiros_x_dias = self.df_performance.iloc[0]

            st.markdown(
                f"""
                Principais métricas de erro calculadas para os primeiros :blue[{metrica_primeiros_x_dias['dias_no_futuro']}] dias
            """
            )

            with st.container():
                col0, col1, col2, col3 = st.columns([1, 1, 1, 1])

                with col0:
                    st.metric(
                        label="MSE",
                        value=format_number(metrica_primeiros_x_dias["mse"], "%0.4f"),
                    )

                with col1:
                    st.metric(
                        label="RMSE",
                        value=format_number(metrica_primeiros_x_dias["rmse"], "%0.4f"),
                    )

                with col2:
                    st.metric(
                        label="MAE",
                        value=format_number(metrica_primeiros_x_dias["mae"], "%0.4f"),
                    )

                with col3:
                    st.metric(
                        label="MAPE",
                        value=format_number(
                            metrica_primeiros_x_dias["mape"] * 100, "%0.4f"
                        )
                        + "%",
                    )

            self.plot_grafico_performance()

            min = DATA_INICIAL
            max_date = DATA_INICIAL + timedelta(days=90)
            end_date = st.date_input(
                "Data máxima de previsão",
                min_value=min,
                max_value=max_date,
                value=max_date,
            )

            if st.button(":crystal_ball: Prever"):
                with st.spinner("Processando..."):
                    time.sleep(3)

                    date_difference = min - (end_date)
                    days_between = np.abs(date_difference.days)

                    st.write(days_between)

                    df_futuro = self.modelo.make_future_dataframe(
                        periods=days_between, freq="D"
                    )
                    self.df_previsao = self.modelo.predict(df_futuro)
                    self.plot_grafico_previsao()

                    # pega x previsões, filtrando pela data para mostrar ao usuário os próximos valores previstos
                    df_previsoes_iniciais = self.df_previsao.query("ds >= @min and ds <= @end_date")
                    st.dataframe(df_previsoes_iniciais[["ds", "yhat"]].iloc[0:10])

                    st.success("Processamento concluído!")
