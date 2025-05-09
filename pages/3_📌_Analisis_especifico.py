import streamlit as st
import pandas as pd


# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Analisis especifico")

nombre = st.text_input("Escribe tu nombre:")


if nombre:
    st.markdown(
        "### 👋 ¡Hola! "
        + nombre
        + " esperamos que disfrutes explorando nuestros filtros 🎉"
    )

