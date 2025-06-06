import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Filtros interactivos")

csv_path = 'pages/static/dataset/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv'
df = pd.read_csv(csv_path)

def aplicar_filtros(df):
    with st.sidebar:
        st.header("🔍 Filtros Interactivos")
        
        # 1. Filtro por sexo
        opciones_sexo = ['Todos'] + df['SEXO FALLECIDO'].unique().tolist()
        sexo = st.selectbox("Sexo del fallecido", opciones_sexo)
        
        # 2. Filtro por edad
        min_edad, max_edad = st.slider(
            "Rango de edad",
            min_value=int(df['EDAD FALLECIDO'].min()),
            max_value=int(df['EDAD FALLECIDO'].max()),
            value=(int(df['EDAD FALLECIDO'].min()), int(df['EDAD FALLECIDO'].max()))  # Valor inicial ajustado a los datos reales
        )
        
        # 3. Filtro por causa directa
        causas = ['Todas'] + df['CAUSA DIRECTA'].unique().tolist()
        causa = st.selectbox("Causa directa", causas)
        
        # 4. Filtro por departamentos
        departamentos = st.multiselect(
            "Departamentos",
            options=df['DEPARTAMENTO RESIDENCIA'].unique(),
            default=['ANTIOQUIA']
        )
        
        # 5. Filtro por trimestre
        if 'Trimestre' in df.columns:
            trimestre = st.selectbox("Trimestre", options=[1, 2, 3, 4, 'Todos'])
        
        # 6. Filtro por nivel educativo
        educacion_opciones = ['Todos', 'Con registro', 'Sin registro']
        educacion = st.selectbox("Nivel educativo", educacion_opciones)
    
    # Aplicar filtros
    df_filtrado = df.copy()
    
    # Filtro sexo
    if sexo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['SEXO FALLECIDO'] == sexo]
    
    # Filtro edad
    df_filtrado = df_filtrado[
        (df_filtrado['EDAD FALLECIDO'] >= min_edad) & 
        (df_filtrado['EDAD FALLECIDO'] <= max_edad)
    ]
    
    # Filtro causa
    if causa != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['CAUSA DIRECTA'] == causa]
    
    # Filtro departamentos
    if departamentos:
        df_filtrado = df_filtrado[df_filtrado['DEPARTAMENTO RESIDENCIA'].isin(departamentos)]
    
    # Filtro trimestre
    if 'Trimestre' in df.columns and trimestre != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Trimestre'] == trimestre]
    
    # Filtro educación
    if educacion == 'Sin registro':
        df_filtrado = df_filtrado[df_filtrado['NIVEL EDUCATIVO FALLECIDO'].isna()]
    elif educacion == 'Con registro':
        df_filtrado = df_filtrado[~df_filtrado['NIVEL EDUCATIVO FALLECIDO'].isna()]
    
    return df_filtrado

# Interfaz principal
st.subheader("Análisis de Defunciones - Hospital General de Medellín 2022-2023")

# Aplicar filtros
df_filtrado = aplicar_filtros(df)

# Mostrar resultados
st.write(f"Filtro inicial con sidebar para poder evidenciar reportes en cuanto a la edad,las causas directas y el departamento")
st.subheader("Resultados Filtrados")
st.write(f"Registros encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado, height=400)

# Sección de filtros combinados
with st.expander("Filtros Avanzados"):
    st.subheader("Combinaciones Específicas")
    # 2. Accidentes por departamento
    if st.checkbox("Mostrar accidentes por departamento"):
        col1, col2 = st.columns(2)
        with col1:
            depto_accidente = st.selectbox("Departamento", df['DEPARTAMENTO RESIDENCIA'].unique())
        with col2:
            causa_accidente = st.selectbox("Tipo de accidente", df['CAUSA DIRECTA'].unique())
        
        filtro_accidentes = (
            (df_filtrado['DEPARTAMENTO RESIDENCIA'] == depto_accidente) &
            (df_filtrado['CAUSA DIRECTA'] == causa_accidente)
        )
        st.dataframe(df_filtrado[filtro_accidentes])

# Selección por posiciones
st.subheader("Selección por Posiciones")
filas = st.number_input("Número de filas a mostrar", 1, 100, 5)
columnas = st.number_input("Número de columnas a mostrar", 1, len(df.columns), 3)

if st.button("Mostrar segmento"):
    df_segmento = df.iloc[0:filas, 0:columnas]
    st.dataframe(df_segmento)

if st.checkbox("Categorización Tipo de defunción reportada"):
    # Crear lista de opciones (incluye todos los valores únicos del campo)
    opciones_tipo = ['Todos'] + df['TIPO DEFUNCION'].dropna().unique().tolist()
    
    # Selectbox para elegir el tipo
    tipo_elegido = st.selectbox(
        "Filtrar por Tipo de Defunción:",
        opciones_tipo,
        key="filtro_tipo_defuncion"  
    )
    
    # Aplicar filtro al DataFrame ORIGINAL 
    if tipo_elegido != 'Todos':
        df_tipo = df[df['TIPO DEFUNCION'] == tipo_elegido]
    else:
        df_tipo = df  # Mostrar todos si no se aplica filtro
    
    # Mostrar resultados
    st.write(f"Defunciones tipo: **{tipo_elegido}**")
    st.dataframe(df_tipo)