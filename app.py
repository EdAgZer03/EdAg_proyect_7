# Importa las bibliotecas necesarias para el análisis de datos, visualización y creación de la aplicación web

import pandas as pd
import plotly.graph_objects as go  # type: ignore
import streamlit as st

# Carga el dataset
df = pd.read_csv(
    'C:\\Users\\ZeroZ\\TT_proyects\\my_proyect_7\\vehicles_us.csv')

# "===============Estructura de Titulo y Subtitulo inicial================="

# Agrega un título a la aplicación
st.title("Vizualización de datos con Streamlit y Plotly")

# "===============Analisis Exploratorio con DataFrame================="

st.header("Análisis Exploratorio de Datos (EDA)")

st.subheader("Vista previa del dataset")

st.write("En esta sección, exploraremos el dataset de vehículos para entender su estructura y características. A continuación, se muestra una vista previa de los datos, junto con algunas opciones para filtrar y analizar la información.")

# Crea una columna nueva llamada 'brand' extrayendo la marca del vehículo de la columna 'model'
df['brand'] = df['model'].astype(str).str.split().str[0].str.title()

# Filtrar filas donde 'brand' no es nulo ni vacío
df_filtered = df[df['brand'].notna() & (df['brand'] != '')]

# Calcula cuántos anuncios tiene cada marca
df_brand_counts = df_filtered['brand'].value_counts()
brands_over_10000 = df_brand_counts[df_brand_counts > 10000].index.tolist()

# Checkbox para mostrar solo las marcas con más de 10000 anuncios
show_top_brands = st.checkbox("Mostrar solo marcas con más de 10000 anuncios")

if show_top_brands:
    df = df[df['brand'].isin(brands_over_10000)]
    st.write(
        f"Mostrando marcas con más de 10000 anuncios: {len(brands_over_10000)}")

st.dataframe(df)

# "===============Gráfico de Barras con Plotly================="

st.header("Gráfico de Barras: Precio Promedio por Tipo de Vehículo")

st.write("Este gráfico muestra el precio promedio de los vehículos agrupados por tipo. Puedes ver cómo varía el precio según el tipo de vehículo, lo que puede ayudarte a identificar tendencias y patrones en el mercado automotriz. Haz clic en el botón para generar el gráfico de barras.")

bar_button = st.button("Crear gráfico de barras")

if bar_button:
    # Agrupa los datos por tipo de vehículo, calcula el precio promedio y Los ordena de mayor a menor
    avg_price_by_type = df.groupby(
        'type')['price'].mean().sort_values(ascending=False)
    df_grouped = avg_price_by_type.reset_index()

    # Crea un gráfico de barras utilizando Plotly
    Bar_fig = go.Figure()

    # Define un diccionario de colores para cada tipo de vehículo
    colors = {
        'SEDAN': '#3498db',         # Azul
        'PICKUP': "#13dd38",        # Verde lima
        'SUV': '#e74c3c',           # Rojo
        'TRUCK': '#f39c12',         # Naranja
        'COUPE': '#9b59b6',         # Morado
        'VAN': "#39d9e4",           # Azul claro
        'CONVERTIBLE': "#bc81f8",   # Rosa
        'HATCHBACK': '#2ecc71',     # Verde
        'WAGON': '#1abc9c',         # Turquesa
        'MINIVAN': '#d35400',       # Naranja oscuro
        'OTHER': '#7f8c8d'          # Gris
    }

    # Convertir etiquetas a mayúsculas para que coincidan con las claves del diccionario de colores
    x_values = df_grouped['type'].str.upper()
    y_values = df_grouped['price']

    Bar_fig.add_trace(go.Bar(
        x=x_values,
        y=y_values,
        marker_color=[colors.get(t, "#2aadb6") for t in x_values],
        text=[f"${p:,.0f}" for p in y_values],
        textposition='inside',
        textangle=90,  # Rotar texto 90 grados para que sea vertical
        textfont=dict(family='Arial', size=10, color='white'),
        name='Precio promedio'
    ))

    # Actualiza la distribución del gráfico con títulos, estilos y configuración de visualización
    Bar_fig.update_layout(title_text='Precio Promedio por Tipo de Vehículo',
                          title_x=0.35,
                          xaxis_title_text='Tipo de Vehículo', yaxis_title_text='Precio Promedio',
                          xaxis_tickangle=-45,  # Rotar etiquetas del eje x 45 grados
                          yaxis_showgrid=True, yaxis_gridcolor='rgba(200, 200, 200, 0.3)',
                          bargap=0.2
                          )

    # Muestra el gráfico en Streamlit
    st.plotly_chart(Bar_fig)
