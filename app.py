# Importa las bibliotecas necesarias para el análisis de datos, visualización y creación de la aplicación web

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Carga el dataset
df = pd.read_csv(
    'C:\\Users\\ZeroZ\\TT_proyects\\my_proyect_7\\vehicles_us.csv')

# "===============Estructura de Titulo y Subtitulo inicial================="

# Agrega un título a la aplicación
st.title("Vizualización de datos con Streamlit y Plotly")

# "===============Analisis Exploratorio con DataFrame================="

st.header("Análisis Exploratorio de Datos (EDA)")

# Crea una columna nueva llamada 'brand' extrayendo la marca del vehículo de la columna 'model'
df['brand'] = df['model'].astype(str).str.split().str[0].str.title()

# Calcula cuántos anuncios tiene cada marca
df_brand_counts = df['brand'].value_counts()
brands_over_10000 = df_brand_counts[df_brand_counts > 10000].index.tolist()

# Checkbox para mostrar solo las marcas con más de 10000 anuncios
show_top_brands = st.checkbox("Mostrar solo marcas con más de 10000 anuncios")

if show_top_brands:
    df = df[df['brand'].isin(brands_over_10000)]
    st.write(
        f"Mostrando marcas con más de 10000 anuncios: {len(brands_over_10000)}")

st.dataframe(df)

# "===============Gráfico de Barras con Plotly================="

st.subheader("Distribucion de odometro")
