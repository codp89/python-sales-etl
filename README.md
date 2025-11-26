Python Sales ETL

ETL completo (Extraer – Transformar – Cargar) usando Python + pandas

Este proyecto implementa un flujo ETL profesional, ideal para análisis de ventas de e-commerce.
Lee un archivo CSV, limpia y transforma los datos, calcula KPIs, genera reportes y produce gráficos automáticos.

-Características principales

Extracción desde un archivo CSV (data/raw/sales.csv)

Limpieza y normalización de datos con pandas

Cálculo de KPIs:

Ingreso total

Ingreso por mes

Ingreso por categoría

Top 10 productos

Top 10 clientes

Generación de reportes:

CSVs procesados

Gráficos .png en /reports

Resumen en Markdown

Arquitectura modular: extract / transform / load / plots



-Instalación
git clone https://github.com/codp89/python-sales-etl.git
cd python-sales-etl
pip install -r requirements.txt

▶Ejecución del proceso ETL
python main.py


Luego del procesamiento:

Los datos limpios estarán en: data/processed/

Los gráficos estarán en: reports/*.png

El resumen estará en: reports/summary.md

-Ejemplo de KPIs generados

Ingreso total: calculado automáticamente

Ingreso mensual: gráfica lineal

Ingreso por categoría: gráfica de barras

Top productos / clientes: CSV detallado


-Tecnologías usadas

Python 3.x

pandas

matplotlib

pathlib


-Potenciales mejoras

Integración con base de datos

Publicación del reporte final en HTML/PDF

Automatización con Airflow

Agregar Pytest para validar transformaciones

Dashboard en Streamlit (opcional)


-Autor
Cristian Martínez
Full Stack Developer
GitHub: https://github.com/codp89