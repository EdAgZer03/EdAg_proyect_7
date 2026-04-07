# Importa las bibliotecas necesarias para el análisis de datos, visualización y creación de la aplicación web

import pandas as pd
import plotly.graph_objects as go  # type: ignore
import streamlit as st

# Carga el dataset
df = pd.read_csv(
    'vehicles_us.csv')

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

# "===============Gráfico de Dispersión con Plotly================="

# Crear un boton para crear un Grafico de dispersion para mostrar la relacion entre el odometro y el precio.
st.header("Gráfico de Dispersión: Relación entre Odómetro y Precio")

st.write("Este gráfico de dispersión muestra la relación entre el odómetro (kilometraje) y el precio de los vehículos. Cada punto representa un vehículo, y la posición en el eje horizontal indica su kilometraje, mientras que la posición en el eje vertical indica su precio. Puedes usar este gráfico para identificar tendencias, como si los vehículos con mayor kilometraje tienden a tener precios más bajos. Haz clic en el botón para generar el gráfico de dispersión.")

# Botón para crear el gráfico de dispersión
scatter_button = st.button("Crear gráfico de dispersión")

if scatter_button:
    # Crea un gráfico de dispersión utilizando Plotly para mostrar la relación entre odómetro y precio
    scatter_fig = go.Figure(data=go.Scatter(
        x=df['odometer'],  # Valores del eje x: kilometraje del vehículo
        y=df['price'],     # Valores del eje y: precio del vehículo
        mode='markers',    # Modo de visualización: puntos (markers)
        marker=dict(       # Configuración de los marcadores (puntos)
            color='blue',  # Color de los puntos
            size=10,       # Tamaño de los puntos
            opacity=0.6    # Transparencia de los puntos
        )
    ))

    # Actualiza el layout del gráfico con títulos, estilos y configuración de visualización
    scatter_fig.update_layout(title_text='Relación entre Odómetro y Precio',
                              title_x=0.35,  # Posición del título (centrado)
                              xaxis_title_text='Odómetro (km)', yaxis_title_text='Precio ($)',
                              # Grid del eje x
                              xaxis_showgrid=True, xaxis_gridcolor='rgba(200, 200, 200, 0.3)',
                              # Grid del eje y
                              yaxis_showgrid=True, yaxis_gridcolor='rgba(200, 200, 200, 0.3)'
                              )

    # Muestra el gráfico en Streamlit
    st.plotly_chart(scatter_fig)

# "===============Grafico de Histograma con Plotly================="

# Crear un set de Check boxes mas un boton para crear el grafico seleccionado: uno que haga un histograma de "Condicion vs año del modelo" y otro dela distribución del odómetro.
st.header("Gráfico de Histograma: Distribución de Condición vs Año del Modelo y Distribución del Odómetro")
st.write("En esta sección, puedes seleccionar qué histogramas deseas crear para analizar la distribución de la condición de los vehículos en relación con el año del modelo, o la distribución del odómetro. Selecciona las opciones deseadas y haz clic en el botón para generar los gráficos.")

st.checkbox("Condición vs Año del Modelo",
            key="hist_condition_year")
st.checkbox("Distribución del Odómetro",
            key="hist_odometer")

# Botón para crear los histogramas seleccionados
hist_button = st.button("Crear histogramas seleccionados")

if hist_button:
    if st.session_state.hist_condition_year:
        # Crea un gráfico de histograma para mostrar la distribución de la condición de los vehículos en relación con el año del modelo
        hist_condition_year_fig = go.Figure()

        # Agrega un histograma para cada condición de vehículo
        for condition in df['condition'].unique():
            hist_condition_year_fig.add_trace(go.Histogram(
                # Año del modelo para la condición actual
                x=df[df['condition'] == condition]['model_year'],
                name=condition,  # Nombre de la traza (condición)
                opacity=0.75     # Opacidad de las barras
            ))

        # Actualiza el layout del gráfico con títulos, estilos y configuración de visualización
        hist_condition_year_fig.update_layout(title_text='Distribución de Condición vs Año del Modelo',
                                              # Posición del título (centrado)
                                              title_x=0.35,
                                              xaxis_title_text='Año del Modelo', yaxis_title_text='Cantidad de Vehículos',
                                              barmode='overlay',  # Superpone las barras para diferentes condiciones
                                              xaxis_showgrid=True, xaxis_gridcolor='rgba(200, 200, 200, 0.3)',
                                              yaxis_showgrid=True, yaxis_gridcolor='rgba(200, 200, 200, 0.3)'
                                              )

        # Muestra el gráfico en Streamlit
        st.plotly_chart(hist_condition_year_fig)

    if st.session_state.hist_odometer:
        # Crea un gráfico de histograma para mostrar la distribución del odómetro (kilometraje) de los vehículos
        hist_odometer_fig = go.Figure(data=go.Histogram(
            x=df['odometer'],  # Valores del eje x: kilometraje del vehículo
            nbinsx=50,        # Número de bins (barras) en el histograma
            marker_color='green',  # Color de las barras
            opacity=0.75      # Opacidad de las barras
        ))

        # Actualiza el layout del gráfico con títulos, estilos y configuración de visualización
        hist_odometer_fig.update_layout(title_text='Distribución del Odómetro',
                                        # Posición del título (centrado)
                                        title_x=0.35,
                                        xaxis_title_text='Odómetro (km)', yaxis_title_text='Cantidad de Vehículos',
                                        xaxis_showgrid=True, xaxis_gridcolor='rgba(200, 200, 200, 0.3)',
                                        yaxis_showgrid=True, yaxis_gridcolor='rgba(200, 200, 200, 0.3)'
                                        )

        # Muestra el gráfico en Streamlit
        st.plotly_chart(hist_odometer_fig)

# "===============Histograma Comparativo de Precios por Marca================="

st.header("Histograma Comparativo de Precios por Marca")

st.write("Selecciona dos marcas para comparar la distribución de sus precios mediante un histograma. La primera marca se mostrará en rojo y la segunda en azul.")

# Obtener la lista de marcas únicas ordenadas
brand_list = sorted(df_filtered['brand'].unique())

# Selectbox para la primera marca
brand1 = st.selectbox("Selecciona la primera marca", brand_list, key="brand1")

# Selectbox para la segunda marca
brand2 = st.selectbox("Selecciona la segunda marca", brand_list, key="brand2")

# Botón para crear el histograma comparativo
compare_button = st.button("Crear histograma comparativo")

if compare_button:
    # Filtrar los datos para cada marca
    df_brand1 = df_filtered[df_filtered['brand'] == brand1]
    df_brand2 = df_filtered[df_filtered['brand'] == brand2]

    # Crear la figura de Plotly
    compare_fig = go.Figure()

    # Agregar histograma para la primera marca (Azul)
    compare_fig.add_trace(go.Histogram(
        x=df_brand1['price'],
        name=brand1,
        marker_color='blue'
    ))

    # Agregar histograma para la segunda marca (rojo)
    compare_fig.add_trace(go.Histogram(
        x=df_brand2['price'],
        name=brand2,
        marker_color='red'
    ))
    # Actualizar el layout del gráfico
    compare_fig.update_layout(
        title_text=f'Comparación de Precios: {brand1} (Azul) vs {brand2} (Rojo)',
        title_x=0.25,
        xaxis_title_text='Precio ($)',
        yaxis_title_text='Frecuencia',
        barmode='overlay',  # Superponer los histogramas
        xaxis_showgrid=True,
        xaxis_gridcolor='rgba(200, 200, 200, 0.3)',
        yaxis_showgrid=True,
        yaxis_gridcolor='rgba(200, 200, 200, 0.3)'
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(compare_fig)
