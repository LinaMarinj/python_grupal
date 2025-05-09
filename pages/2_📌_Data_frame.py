import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Dataframe")

df = pd.read_csv(
    "pages/static/dataset/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv"
)
st.markdown(
    '<h2 style="color: #0066cc;">Defunciones ocurridas en el Hospital General de Medellín 2022-2023</h3>',
    unsafe_allow_html=True,
)

st.dataframe(df)

