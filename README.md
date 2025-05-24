# Aplicación Streamlit - Pandas

Este proyecto es una aplicación web que tiene como finalidad analizar una base de datos pública mediante el uso de librerías de Python como Streamlit, Pandas, entre otras. A lo largo del desarrollo, se aplicarán métodos de filtrado y técnicas básicas de análisis de datos, aprovechando herramientas interactivas para facilitar la visualización y comprensión de la información.

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

###

# Introducción

En el presente proyecto Se presenta un análisis exploratorio y visual de los datos de defunciones registrados en el Hospital General de Medellín durante los años 2022 y 2023.

# Elementos disponibles para análisis

La base de datos utilizada es de acceso gratuito y contiene información detallada sobre cada caso de fallecimiento, incluyendo variables como:

-Año de defunción
-Sitio y tipo de defunción
-Fecha, sexo y edad del fallecido
-Estado civil, nivel educativo y ocupación
-municipio de residencia
-Muerte y causas

A través del uso de Python, la librería pandas para el análisis de datos y Streamlit para la construcción de una interfaz interactiva, este proyecto busca ofrecer una herramienta sencilla pero poderosa para examinar datos.

## Utilidad del proyecto

Este análisis puede ser útil para investigadores y profesionales de la salud pública interesados en comprender mejor la dinámica de mortalidad en esta institución, así como para personas que deseen conocer las causas de muerte más comunes en Colombia y las enfermedades que llevaron a los decesos en el Hospital General de Medellín durante los años 2022 y 2023.

## Fuente consultada

[https://www.datos.gov.co/] – Hospital General de Medellín. Disponible en: [https://www.datos.gov.co/Salud-y-Protecci-n-Social/Defunciones-ocurridas-en-en-el-Hospital-General-de/hwwv-mhse/about_data]

## Características

- Interfaz de usuario intuitiva y responsive
- Múltiples páginas organizadas por momentos
- Estructura de proyecto organizada y mantenible
- Secciones específicas para cada punto

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona o descarga este repositorio en tu computadora

2. Crea un entorno virtual (opcional pero recomendado):

   ```
   python -m venv .venv
   ```

3. Activa el entorno virtual:

   - En Windows:
     ```
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
pio 
## Uso

Para ejecutar la aplicación:

```
streamlit run Inicio.py
```

La aplicación estará disponible en tu navegador en `http://localhost:8501`.

## Estructura del proyecto

```
├── .streamlit/            # Configuración de Streamlit
│   └── config.toml        # Archivo de configuración (tema, servidor, etc.)
├── assets/                # Recursos estáticos
│   ├── foto.webp           # Foto representativa
│   └── logo-Cesde-2023.svg # Logo de CESDE
├── data/                  # Carpeta para almacenar datos
├── pages/                 # Páginas de la aplicación
│   ├── 1_📌_Proyecto.py              # Introducción al proyecto
│   ├── 2_📌_Data_set.py              # Data
│   ├── 3_📌_Analisis_especifico.py   # Análisis
│   ├── 4_📌_Graficos.py              # Gráficos
├── .gitignore             # Archivos ignorados por Git
├── Inicio.py              # Punto de entrada de la aplicación
├── README.md              # Este archivo
└── requirements.txt       # Dependencias del proyecto
```

## Navegación por la aplicación

1. **Página de inicio (Inicio.py)**: Muestra información general de los participantes.

2. **Proyecto**: Página 1, contiene la introduccion al proyecto.

3. **Data_set**: Página 2, la Data del proyecto.

4. **Analisis_especificos**: Página 3, analisis de los datos

5. **Evaluación del Momento 3**: Página 4, Gráficos.

## Dependencias principales

- streamlit: Framework para crear aplicaciones web interactivas
- pandas: Manipulación y análisis de datos
- numpy: Computación numérica
- matplotlib y seaborn: Visualización de datos
- plotly: Gráficos interactivos

Consulta el archivo `requirements.txt` para ver la lista completa de dependencias.

## Consejos para el desarrollo

- Utiliza la función `st.help()` para obtener ayuda sobre cualquier función de Streamlit.
- Consulta la [documentación oficial de Streamlit](https://docs.streamlit.io/) para más información.
- Utiliza `st.write()` para depurar variables durante el desarrollo.
- Aprovecha los widgets interactivos de Streamlit para hacer tus actividades más dinámicas.
