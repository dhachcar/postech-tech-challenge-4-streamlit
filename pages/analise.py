import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from util.layout import output_layout, format_number


st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

df = pd.read_csv("assets/csv/timeseries-petroleo-brent.csv")

with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")

    st.markdown(
        """
        Após uma análise detalhada do histórico de preços do barril de petróleo, agora estamos explorando como a distribuição desses preços se desenvolve ao longo das décadas, abrangendo desde o início da série histórica estabelecida pela EIA em 1987. Além disso, examinamos indicadores como os níveis de preços mais comuns, as mínimas e máximas históricas, entre outros, os quais são apresentados e discutidos.
    """
    )

    st.subheader(":blue[Análise descritiva]", divider="blue")

    df_descritiva = df.describe()
    medida_count = df_descritiva.loc["count"]["y"]
    medida_mean = df_descritiva.loc["mean"]["y"]
    medida_std = df_descritiva.loc["std"]["y"]
    medida_min = df_descritiva.loc["min"]["y"]
    medida_25 = df_descritiva.loc["25%"]["y"]
    medida_50 = df_descritiva.loc["50%"]["y"]
    medida_75 = df_descritiva.loc["75%"]["y"]
    medida_max = df_descritiva.loc["max"]["y"]
    df_descritiva.reset_index(inplace=True)
    df_descritiva.columns = ["Medidas", "Preço do barril de petróleo"]

    st.markdown(
        f"""
        Nesta seção, apresentamos a análise descritiva da distribuição de preços ao longo das décadas. Como podemos observar, os dados apresentados consistem em um total de :blue[{format_number(medida_count)}] observações, com uma média de aproximadamente :blue[{format_number(medida_mean, '%.2f')}] e um desvio padrão em torno de :blue[{format_number(medida_std, '%.2f')}]. O valor mínimo observado é :blue[{format_number(medida_min, '%.2f')}], enquanto o valor máximo atinge :blue[{format_number(medida_max, '%.2f')}]. Os quartis indicam que 25% dos dados estão abaixo de :blue[{format_number(medida_25, '%.2f')}], 50% abaixo de :blue[{format_number(medida_50, '%.2f')}] (mediana) e 75% abaixo de :blue[{format_number(medida_75, '%.2f')}], proporcionando uma visão abrangente da distribuição e variabilidade dos dados.
    """
    )

    with st.container():
        _, col, _ = st.columns([3, 4, 3])

        with col:
            st.dataframe(df_descritiva, use_container_width=True, hide_index=True)

    st.markdown(
        f"""
        Por fim, apresentamos um boxplot desse dados, de forma a observarmos os dados de uma maneira mais visual. Também apresentamos um histograma a respeito da distribuição, onde podemos observar que definitivamente a distribuição não é normal.
    """
    )

    with st.container():
        col0, col1 = st.columns([3, 7])

        with col0:
            st.subheader(":blue[Boxplot]", divider="blue")

            fig = go.Figure(
                layout=go.Layout(
                    xaxis=dict(title="Data"),
                    yaxis=dict(title="Preço em US$"),
                    height=600,
                ),
            )

            fig.add_trace(
                go.Box(
                    y=df.y,
                    name="Preço do barril de petróleo Brent",
                    hoverlabel=dict(align="right"),
                    boxmean=True,
                )
            )

            st.plotly_chart(fig, use_container_width=True)

        with col1:
            st.subheader(":blue[Histograma]", divider="blue")

            fig = ff.create_distplot([df.y], group_labels=["Distribuição dos preços"])
            fig.update_layout(
                xaxis_title="Valor",
                yaxis_title="Densidade",
                height=600,
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
                ),
            )
            fig.data[1].line.color = "red"

            st.plotly_chart(fig, use_container_width=True)
