import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")


st.header("🏥Defunciones ocurridas en el Hospital General de Medellín")

st.subheader("Descripción de la actividad")
st.markdown(
    """
Esta actividad tiene como finalidad analizar una base de datos pública mediante el uso de librerías de Python
como Streamlit y Pandas. A lo largo del desarrollo, se aplicarán métodos de filtrado y técnicas básicas de análisis de datos, 
aprovechando herramientas interactivas para facilitar la visualización y comprensión de la información.
"""
)

import streamlit as st

st.markdown('<h3 style="color: #0066cc;">Solución</h3>', unsafe_allow_html=True)

df = pd.read_csv(
    "pages/static/dataset/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv"
)


st.markdown(
    """
### Introducción

Este proyecto tiene como objetivo explorar, analizar y visualizar los datos de defunciones ocurridas en el Hospital General de Medellín entre los años 2022 y 2023. 

**Elementos disponibles para análisis**

La base de datos utilizada es de acceso gratuito y contiene información detallada sobre cada caso de fallecimiento, incluyendo variables como:

- Año de defunción
- Sitio y tipo de defunción
- Fecha, sexo y edad del fallecido
- Estado civil, nivel educativo y ocupación
- municipio de residencia
- Muerte y causas

A través del uso de Python, la librería **pandas** para el análisis de datos y **Streamlit** para la construcción de una interfaz interactiva, este proyecto busca ofrecer una herramienta sencilla pero poderosa para examinar datos.
"""
)

st.markdown(
    """
    <div style="text-align: justify;">
    <h3>Utilidad del proyecto</h3>
    Este análisis puede ser útil para investigadores y profesionales de la salud pública interesados
    en comprender mejor la dinámica de mortalidad en esta institución, así como para personas que deseen conocer
    las causas de muerte más comunes en Colombia y las enfermedades que llevaron a los decesos en el Hospital General de Medellín durante los años 2022 y 2023.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<br><p style="color: #0066cc;">Datos suministrados por: </p>',
    unsafe_allow_html=True,
)

st.code(
    "https://www.datos.gov.co/Salud-y-Protecci-n-Social/Defunciones-ocurridas-en-en-el-Hospital-General-de/hwwv-mhse/about_data",
    language="text",
)
