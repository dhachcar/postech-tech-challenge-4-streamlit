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
    
    st.markdown(
        """
        1. Brent – O que é, significado e definição. Disponível em: https://guru.com.vc/glossario/brent/. Acesso em: 04/04/2024.
        2. EIA. Disponível em: https://www.eia.gov/. Acesso em: 02/04/2024.
        3. EIA Developer. Disponível em: https://www.eia.gov/developer/. Acesso em: 02/04/2024.
        4. EIA Petroleum API Dashboard. Disponível em: https://www.eia.gov/opendata/browser/petroleum/pri/spt. Acesso em: 02/04/2024.
        5. Entenda a queda do preço do petróleo e seus efeitos. Publicado em: 16/01/2015. Disponível em: https://g1.globo.com/economia/noticia/2015/01/entenda-queda-do-preco-do-petroleo-e-seus-efeitos.html. Acesso em: 18/04/2024.
        6. IPEA. Publicado em: 2022. Disponível em: https://www.ipea.gov.br/portal/. Acesso em: 02/04/2024.
        7. JUNIOR, J. R. F. Redes Neurais Recorrentes — LSTM. Publicado em: 11/06/2019. Disponível em: https://medium.com/@web2ajax/redes-neurais-recorrentes-lstm-b90b720dc3f6. Acesso em: 02/05/2024.
        8. JÚNIOR, C. O. Métricas para Regressão: Entendendo as métricas R², MAE, MAPE, MSE e RMSE. Publicado em: 12/12/2021. Disponível em: https://medium.com/data-hackers/prevendo-n%C3%BAmeros-entendendo-m%C3%A9tricas-de-regress%C3%A3o-35545e011e70. Acesso em: 29/04/2024.
        9. Keras About. Disponível em: https://keras.io/about/. Acesso em: 02/04/2024.
        10. Meta Prophet Quick Start. Disponível em: https://facebook.github.io/prophet/docs/quick_start.html. Acesso em: 23/04/2024.
        11. OLIVEIRA, K. Agência Brasil. Economia segue em recuperação com crescimento robusto, diz secretaria. Publicado em: 02/06/2022. Disponível em: https://agenciabrasil.ebc.com.br/economia/noticia/2022-06/economia-segue-em-recuperacao-com-crescimento-robusto-diz-secretaria. Acesso em: 01/05/2024.
        12. Opep mantém teto de produção inalterado. Publicado em: 27/11/2014. Disponível em: https://economia.uol.com.br/noticias/afp/2014/11/27/opep-mantem-teto-de-producao-inalterado.htm. Acesso em: 15/04/2024.
        13. PENTEADO, K. Métricas de avaliação para séries temporais. Publicado em: 09/06/2021. Disponível em: https://www.alura.com.br/artigos/metricas-de-avaliacao-para-series-temporais. Acesso em: 29/04/2024.
        14. Plotly. Disponível em: https://plotly.com/python. Acesso em: 23/04/2024.
        15. Tensorflow. Disponível em: https://www.tensorflow.org/?hl=pt-br. Acesso em: 02/04/2024.
        16. Tensorflow Keras. Disponível em: https://www.tensorflow.org/guide/keras?hl=pt-br. Acesso em: 02/04/2024.
        17. Wikipedia. Ataques de 11 de Setembro de 2001. Disponível em: https://pt.wikipedia.org/wiki/Ataques_de_11_de_setembro_de_2001. Acesso em: 06/04/2024.
        18. Wikipedia. Crise Financeiro de 2007-2008. Disponível em: https://pt.wikipedia.org/wiki/Crise_financeira_de_2007%E2%80%932008. Acesso em: 07/04/2024.
        19. Wikipedia. Guerra Civil Líbia. Disponível em: https://pt.wikipedia.org/wiki/Guerra_Civil_L%C3%ADbia_(2011). Acesso em: 08/04/2024.
        20. Wikipedia. Guerra Civil Síria em: https://pt.wikipedia.org/wiki/Guerra_Civil_S%C3%ADria. Acesso em: 06/04/2024.
        21. Wikipedia. Guerra do Golfo. Disponível em: https://pt.wikipedia.org/wiki/Guerra_do_Golfo. Acesso em: 06/04/2024.
        22. Wikipedia. Guerra do Iraque. Disponível em: https://pt.wikipedia.org/wiki/Guerra_do_Iraque. Acesso em: 06/04/2024.
        23. Wikipedia. Invasão da Ucránia pela Rússia. Disponível em: https://pt.wikipedia.org/wiki/Invas%C3%A3o_da_Ucr%C3%A2nia_pela_R%C3%BAssia_(2022%E2%80%93presente). Acesso em: 18/04/2024.
        24. Wikipedia. Primavera Árabe em: https://pt.wikipedia.org/wiki/Primavera_%C3%81rabe. Acesso em: 07/04/2024.
        25. Wikipedia. Pandemia de COVID-19. Disponível em: https://pt.wikipedia.org/wiki/Pandemia_de_COVID-19. Acesso em: 09/04/2024.
        26. WOLFFENBÜTTEL, A. O que é? - Petróleo Brent e WTI. Publicado em: 01/11/2005. Disponível em: https://www.ipea.gov.br/desafios/index.php?option=com_content&view=article&id=2083:catid=28&Itemid=23. Acesso em: 04/04/2024.
    """
    )
