import streamlit as st
from st_pages import show_pages, Page
import locale

from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_HISTORIA, TITULO_INTRODUCAO, TITULO_MODELO, TITULO_REFERENCIAS

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./main.py", "Tech Challenge 4", ":house:", use_relative_hash=True),
            Page("./pages/intro.py", TITULO_INTRODUCAO, ":books:", use_relative_hash=True),
            Page("./pages/historia.py", TITULO_HISTORIA, ":open_book:", use_relative_hash=True),
            Page(
                "./pages/analise.py",
                TITULO_ANALISE_EXPLORATORIA,
                ":memo:",
                use_relative_hash=True,
            ),
            Page("./pages/modelo.py", TITULO_MODELO, ":robot_face:", use_relative_hash=True),
            Page(
                "./pages/refs.py",
                TITULO_REFERENCIAS,
                ":globe_with_meridians:",
                use_relative_hash=True,
            ),
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Danilo Henrique Achcar")
        st.text("RM 351516 | 2DTAT")

        st.divider()

        st.subheader("Instalando as dependências do app")
        st.code(body="python -m venv venv", language="shell")
        st.code(body="source venv/Scripts/activate", language="shell")
        st.code(body="pip install -r requirements.txt", language="shell")

        st.divider()

        st.subheader("Executando localmente")
        st.code(body="streamlit run main.py", language="shell")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/dhachcar/postech-tech-challenge-4-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook",
            "https://github.com/dhachcar/postech-tech-challenge-4",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
