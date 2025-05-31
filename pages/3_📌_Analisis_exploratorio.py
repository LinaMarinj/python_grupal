import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Analisis exploratorio")


csv_path = 'pages/static/dataset/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv'
df = pd.read_csv(csv_path)

st.subheader("Vista previa de los datos")
st.dataframe(df.head())

st.subheader("Información general del DataFrame")
info_general = pd.DataFrame({
    "Columna": df.columns,
    "Tipo de dato": [str(df[col].dtype) for col in df.columns],
    "Valores únicos": [int(df[col].nunique()) for col in df.columns],
    "Ejemplo": [", ".join(map(str, df[col].dropna().unique()[:3])) for col in df.columns]
})
st.dataframe(info_general)

st.subheader("Estadísticas descriptivas")
st.write(df.describe(include='all'))

st.subheader("Valores nulos por columna")
st.write(df.isnull().sum())

st.subheader("Estadísticas descriptivas")
st.write(df.describe(include='all'))

if 'EDAD FALLECIDO' in df.columns:
    edad_min = int(df['EDAD FALLECIDO'].min())
    edad_max = int(df['EDAD FALLECIDO'].max())
    edad_seleccionada = st.slider("Selecciona la edad del fallecido", edad_min, edad_max, edad_min)
    df_filtrado_edad = df[df['EDAD FALLECIDO'] == edad_seleccionada]

    st.subheader(f"Defunciones con edad {edad_seleccionada} años")
    st.dataframe(df_filtrado_edad)
else:
    st.warning("La columna 'EDAD FALLECIDO' no existe en el DataFrame.")


if 'AÑO' in df.columns:
    años_disponibles = sorted(df['AÑO'].dropna().unique())
    año_seleccionado = st.selectbox("Selecciona el año de defunción", años_disponibles)
    df_filtrado = df[df['AÑO'] == año_seleccionado]

    st.subheader(f"Defunciones en el año {año_seleccionado}")
    st.dataframe(df_filtrado)
else:
    st.warning("La columna 'AÑO DEFUNCION' no existe en el DataFrame.")

if 'SEXO FALLECIDO' in df.columns:
    sexos_validos = ['MASCULINO', 'FEMENINO']
    df_sexos_validos = df[df['SEXO FALLECIDO'].isin(sexos_validos)]
    sexos_disponibles = df_sexos_validos['SEXO FALLECIDO'].unique()
    sexo_seleccionado = st.selectbox("Selecciona el sexo del fallecido", sexos_disponibles)
    df_filtrado_sexo = df_sexos_validos[df_sexos_validos['SEXO FALLECIDO'] == sexo_seleccionado]

    st.subheader(f"Defunciones de sexo {sexo_seleccionado}")
    st.dataframe(df_filtrado_sexo)
else:
    st.warning("La columna 'SEXO FALLECIDO' no existe en el DataFrame.")

if 'DEPARTAMENTO RESIDENCIA' in df.columns:
    departamentos_disponibles = sorted(df['DEPARTAMENTO RESIDENCIA'].dropna().unique())
    departamento_seleccionado = st.selectbox("Selecciona el departamento", departamentos_disponibles)
    df_filtrado_departamento = df[df['DEPARTAMENTO RESIDENCIA'] == departamento_seleccionado]

    st.subheader(f"Defunciones en el departamento {departamento_seleccionado}")
    st.dataframe(df_filtrado_departamento)
else:
    st.warning("La columna 'DEPARTAMENTO RESIDENCIA' no existe en el DataFrame.")

st.subheader("Defunciones por año (tabla)")
if 'AÑO' in df.columns:
    st.dataframe(df['AÑO'].value_counts().sort_index())
