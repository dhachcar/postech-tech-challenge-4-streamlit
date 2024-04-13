import streamlit as st
from tabs.tab import TabInterface

class ModeloProphetTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.write('teste1')

# with open('db/prophet/prophet-model.json', 'r') as fin:
#             modelo = model_from_json(fin.read()) 
#             df_futuro = modelo.make_future_dataframe(periods=90, freq='D')
#             previsao = modelo.predict(df_futuro)

#             plot_prophet = plot_plotly(modelo, previsao)
            
#             st.plotly_chart(plot_prophet)