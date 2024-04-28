import streamlit as st
from tabs.tab import TabInterface
import joblib
from keras.models import load_model


class ModeloLSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.modelo = load_model("assets/modelos/lstm/lstm")
        self.scaler = joblib.load("assets/modelos/lstm/lstm-scaler.pkl")

        self.render()

    def render(self):
        with self.tab:
            st.write("teste2")
