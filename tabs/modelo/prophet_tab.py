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

        with st.container():
            _, col, _ = st.columns([2, 6, 2])

            with col:
                st.plotly_chart(fig, use_container_width=True)

    def plot_grafico_previsao(self, total_dias_previsao):
        # gráfico do plotly
        fig = plot_plotly(
            self.modelo,
            self.df_previsao,
            trend=True,
            figsize=(1200, 900),
            xlabel="Data",
            ylabel="Preço do barril de petróleo (US$)",
        )

        # objetos de linha
        linha_azul = go.Scatter(
            x=[2020, self.df_previsao.iloc[-1, :].ds],
            y=[0, 0],
            mode="lines",
            line=dict(color="#49d7ff"),
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
            title=f"Distribuição do valor (US$) do barril de petróleo Brent entre 2020 e os dias atuais + previsão dos próximos {total_dias_previsao} dia(s)",
            showlegend=True,
            margin=dict(t=150),
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
            ),
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

        st.plotly_chart(fig, use_container_width=True)

    def output_metricas_erro(self, metricas, primeiros_x_dias):
        st.subheader(
            f":blue[Métricas de erro para os primeiros :orange[{primeiros_x_dias}] dias]",
            divider="blue",
        )

        with st.container():
            (
                col0,
                col1,
            ) = st.columns([1, 1])

            with col0:
                st.metric(
                    label="MSE",
                    value=format_number(metricas["mse"], "%0.4f"),
                )

            with col1:
                st.metric(
                    label="RMSE",
                    value=format_number(metricas["rmse"], "%0.4f"),
                )

        with st.container():
            (
                col0,
                col1,
            ) = st.columns([1, 1])

            with col0:
                st.metric(
                    label="MAE",
                    value=format_number(metricas["mae"], "%0.4f"),
                )

            with col1:
                st.metric(
                    label="MAPE",
                    value=format_number(metricas["mape"] * 100, "%0.4f") + "%",
                )

    def predict(self, min, end_date):
        date_difference = min - end_date
        days_between = np.abs(date_difference.days)

        df_futuro = self.modelo.make_future_dataframe(periods=days_between, freq="D")
        self.df_previsao = self.modelo.predict(df_futuro)

        # pega x previsões, filtrando pela data para mostrar ao usuário os próximos valores previstos
        df_previsoes_iniciais = self.df_previsao.query("ds >= @min and ds <= @end_date")

        with st.container():
            clone = df_previsoes_iniciais.copy()
            clone["ds"] = clone["ds"].apply(
                lambda x: pd.to_datetime(x).strftime("%d/%m/%Y")
            )
            clone.rename(columns={"ds": "Data", "yhat": "Preço"}, inplace=True)

            _, col, _ = st.columns([3, 4, 3])

            with col:
                st.dataframe(
                    clone[["Data", "Preço"]],
                    use_container_width=True,
                    hide_index=True,
                )

        with st.container():
            self.plot_grafico_previsao(total_dias_previsao=days_between)

    def render(self):
        metrica_primeiros_x_dias = self.df_performance.iloc[0]
        metrica_primeiros_15_dias = self.df_performance.iloc[14]
        metrica_primeiros_30_dias = self.df_performance.iloc[29]

        with self.tab:
            st.subheader(":blue[Sobre do modelo]", divider="blue")

            st.markdown(
                """
                Este modelo foi criado utilizando o :blue[Prophet da Meta] e com base nos dados históricos do preço do barril de petróleo Brent a partir de :blue[01/01/2020], de forma a diminuir a janela de treino e consequentemente aumentar a precisão de previsão.
            """
            )

            st.subheader(":blue[Performance do modelo]", divider="blue")

            st.markdown(
                f"""
                Nesta seção, apresentamos os indicadores de erro do modelo :blue[Prophet] criado. Todos eles são gerados de forma automática pela biblioteca e dentre os considerados, estão:
                * :orange[MSE (Mean Squared Error)]: calculado como a média dos quadrados das diferenças entre os valores previstos pelo modelo e os valores reais observados nos dados de teste ou validação. Quanto menor o valor, mais preciso é o modelo em suas previsões.
                * :orange[RMSE (Root Mean Squared Error)]: calculado como a raiz quadrada do MSE, o que significa que fornece uma medida do erro médio entre os valores previstos pelo modelo e os valores reais observados nos dados de teste ou validação, na mesma unidade que os dados originais. Assim como o MSE, quanto menor o valor do RMSE, melhor o desempenho do modelo em fazer previsões precisas.
                * :orange[MAE (Mean Absolute Error)]: calculado como a média das diferenças absolutas entre os valores previstos pelo modelo e os valores reais observados nos dados de teste ou validação. Ao contrário do MSE e do RMSE, o MAE não leva em conta o quadrado das diferenças, o que o torna menos sensível a outliers e mais intuitivo em termos de interpretação, pois representa diretamente a magnitude média dos erros. Quanto menor o valor, melhor.
                * :orange[MAPE (Mean Absolute Percentage Error)]: calculado como a média das diferenças percentuais absolutas entre os valores previstos pelo modelo e os valores reais observados nos dados de teste ou validação. Como os outros, quanto menor, melhor.
                * :orange[MDAPE (Median Absolute Percentage Error)]: calculado como a mediana das diferenças percentuais absolutas entre os valores previstos pelo modelo e os valores reais observados nos dados de teste ou validação. Quanto menor, melhor.
                * :orange[SMAPE (Symmetric Mean Absolute Percentage Error)]: calculado como a média das diferenças percentuais absolutas entre os valores previstos pelo modelo e os valores reais observados nos dados de teste ou validação, levando em consideração o valor absoluto da soma dos valores previstos e reais. Valores menores, indicam previsões mais precisas.
                        
                Vale notar que o modelo teve suas validações efetuadas com base na data de :blue[{DATA_INICIAL.strftime("%d/%m/%Y")}], portanto a performance auferida pela biblioteca começa a ser considerada a partir de 9 dias no futuro, mais especificamente em :blue[{(DATA_INICIAL + timedelta(days=9)).strftime("%d/%m/%Y")}].
            """
            )

            with st.container():
                col0, col1 = st.columns([6, 4])

                with col0:
                    clone = self.df_performance.copy()
                    clone["data_no_futuro"] = clone["data_no_futuro"].apply(
                        lambda x: pd.to_datetime(x).strftime("%d/%m/%Y")
                    )

                    st.dataframe(clone, hide_index=True, height=720)

                with col1:
                    self.output_metricas_erro(
                        metrica_primeiros_x_dias,
                        primeiros_x_dias=metrica_primeiros_x_dias["dias_no_futuro"],
                    )

                    self.output_metricas_erro(
                        metrica_primeiros_15_dias,
                        primeiros_x_dias=metrica_primeiros_15_dias["dias_no_futuro"],
                    )

                    self.output_metricas_erro(
                        metrica_primeiros_30_dias,
                        primeiros_x_dias=metrica_primeiros_30_dias["dias_no_futuro"],
                    )

            st.markdown(
                f"""
                Como podemos observar, quanto maior a janela de tempo no futuro, maiores são as métricas de erro, dado o período de treinamento considerado pelo modelo.\n\n
                Tal relação de tempo X erro pode ser melhor visualizada no gráfico a seguir. Vale notar que os valores foram transformados em seus logaritmos para eliminar discrepâncias entre as diferentes métricas calculadas.
            """
            )

            self.plot_grafico_performance()

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
                        key="dt_input_prophet",
                        min_value=min,
                        max_value=max_date,
                        value=max_date,
                    )

                if st.button(":crystal_ball: Prever", key="btn_predict_prophet"):
                    with st.spinner("Processando..."):
                        time.sleep(3)

                        st.subheader(":blue[Previsão]", divider="blue")

                        st.markdown(
                            f"**:orange[IMPORTANTE:] a previsão é feita com a data base em :blue[{DATA_INICIAL.strftime('%d/%m/%Y')}] (último preço do barril de petróleo coletado).**"
                        )

                        self.predict(min, end_date)

                        st.success("Processamento concluído! :white_check_mark:")
