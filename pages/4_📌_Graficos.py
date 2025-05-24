import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Configuración básica
st.set_page_config(page_icon="📌", layout="wide")

st.title("Gráficos")
st.title("Visualización de Datos Hospitalarios")

# Carga de datos
data = pd.read_csv('pages\static\dataset\Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv')

# Sidebar simple
with st.sidebar:
    st.header("Filtros Básicos")
    edad_min = int(data['EDAD FALLECIDO'].min())
    edad_max = int(data['EDAD FALLECIDO'].max())
    rango_edad = st.slider("Rango de Edad", edad_min, edad_max, (edad_min, edad_max))

# Filtrar datos
datos_filtrados = data[(data['EDAD FALLECIDO'] >= rango_edad[0]) & (data['EDAD FALLECIDO'] <= rango_edad[1])]

# Sección de gráficos
st.header("Gráficos Principales")

# 1. Gráfico de barras por sexo
fig1 = px.histogram(datos_filtrados, x='SEXO FALLECIDO', title='Distribución por Sexo')
st.plotly_chart(fig1, use_container_width=True)

# 2. Histograma de edades
fig2 = px.histogram(datos_filtrados, x='EDAD FALLECIDO', nbins=20, title='Distribución de Edades')
st.plotly_chart(fig2, use_container_width=True)

# 3. Gráfico de causas
fig3 = px.bar(datos_filtrados['CAUSA DIRECTA'].value_counts().head(10), 
             orientation='h', 
             title='Top 10 Causas Directas')
st.plotly_chart(fig3, use_container_width=True)

# 4. Gráfico por departamento
fig4 = px.pie(datos_filtrados, names='DEPARTAMENTO RESIDENCIA', title='Distribución por Departamento')
st.plotly_chart(fig4, use_container_width=True)

# 5. Gráfico temporal (si existe la columna)
fig5 = px.line(datos_filtrados['FECHA DEFUNCION'].value_counts(), 
              title='Evolución Temporal de Defunciones')
st.plotly_chart(fig5, use_container_width=True)

