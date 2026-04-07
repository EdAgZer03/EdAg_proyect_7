# EdAg_proyect_7

## Descripción técnica
Esta aplicación usa `Streamlit` como marco web para presentar un análisis exploratorio de un dataset de vehículos y un gráfico de barras interactivo generado con `Plotly`.

El flujo de la aplicación es el siguiente:
- Carga el dataset `vehicles_us.csv` en un `DataFrame` de `pandas`.
- Extrae la marca del vehículo desde la columna `model` y la normaliza con `title()`.
- Filtra valores nulos o vacíos en la columna `brand`.
- Calcula la frecuencia de marcas y permite al usuario activar un checkbox para mostrar solo marcas con más de `10000` anuncios.
- Muestra el `DataFrame` resultante en un `st.dataframe`.
- Genera un gráfico de barras que muestra el precio promedio por tipo de vehículo (`type`) solo cuando el usuario presiona el botón.
- El gráfico usa colores personalizados por tipo de vehículo, etiquetas de precio dentro de las barras y formato visual adaptado para legibilidad.
- Genera un gráfico de dispersión interactivo para analizar la relación entre el kilometraje (odómetro) y el precio.
- Permite al usuario elegir mediante checkboxes qué histogramas visualizar: "Condición vs Año del Modelo" o "Distribución del Odómetro".
- Incluye un histograma comparativo que permite seleccionar dos marcas diferentes mediante menús desplegables para comparar visualmente sus distribuciones de precios.

## Características
- Vista previa interactiva del dataset.
- Filtrado dinámico de marcas con más de 10000 anuncios.
- Gráfico de barras de precio promedio por tipo de vehículo.
- Gráfico de dispersión para análisis de tendencias entre precio y kilometraje.
- Histogramas configurables para análisis de condición y año.
- Herramienta de comparación de precios entre marcas específicas.
- Visualización basada en `Plotly` para interacción y estilo.

## Dependencias
Las librerías necesarias están listadas en `requirements.txt`:
- `pandas`
- `plotly`
- `streamlit`

## Cómo ejecutar
1. Instalar dependencias:
```bash
pip install -r requirements.txt
```
2. Ejecutar la aplicación Streamlit:
```bash
streamlit run app.py
```

## Nota
Asegúrate de que el archivo `vehicles_us.csv` esté accesible desde la ruta configurada en `app.py`.
