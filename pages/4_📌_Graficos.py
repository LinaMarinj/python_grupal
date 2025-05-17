import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Gráficos")


data = pd.DataFrame({
    'Categoría': ['Edad', 'Genero', 'Municipio', 'estado civil', 'causa directa'],  
    'Valor': [10, 24, 36, 28, 15],
    'Grupo': ['Edad', 'Genero', 'Municipio', 'estado civil', 'causa directa'] 
})

#t.subheader("python_grupal/pages/static/dataset/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv")
plt.figure(figsize=(8, 6))
plt.bar(data['Categoría'], data['Valor'])
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de Barras de las Defunciones ocurridas en el hospital')
st.pyplot(plt)

