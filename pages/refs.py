import streamlit as st
from util.constantes import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFERENCIAS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_REFERENCIAS}]")

    st.markdown('''
        1. https://pt.wikipedia.org/wiki/Guerra_do_Golfo
        2. https://pt.wikipedia.org/wiki/Ataques_de_11_de_setembro_de_2001
        3. https://pt.wikipedia.org/wiki/Guerra_do_Iraque
        4. https://pt.wikipedia.org/wiki/Crise_financeira_de_2007%E2%80%932008
        5. https://pt.wikipedia.org/wiki/Primavera_%C3%81rabe
        6. https://pt.wikipedia.org/wiki/Guerra_Civil_L%C3%ADbia_(2011)
        7. https://pt.wikipedia.org/wiki/Guerra_Civil_S%C3%ADria
        8. https://economia.uol.com.br/noticias/afp/2014/11/27/opep-mantem-teto-de-producao-inalterado.htm
        9. https://g1.globo.com/economia/noticia/2015/01/entenda-queda-do-preco-do-petroleo-e-seus-efeitos.html#:~:text=Os%20principais%20apontados%20como%20%22culpados,na%20Europa%20e%20na%20%C3%81sia
        10. https://pt.wikipedia.org/wiki/Pandemia_de_COVID-19
        11. https://agenciabrasil.ebc.com.br/economia/noticia/2022-06/economia-segue-em-recuperacao-com-crescimento-robusto-diz-secretaria
        12. https://pt.wikipedia.org/wiki/Invas%C3%A3o_da_Ucr%C3%A2nia_pela_R%C3%BAssia_(2022%E2%80%93presente)
    ''')