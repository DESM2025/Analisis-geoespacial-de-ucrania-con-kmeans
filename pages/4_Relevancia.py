import streamlit as st
from pages.utils.ui_theme import centered_image, setup_page

setup_page("Relevancia")

st.title("Relevancia")

st.markdown(
    """
Desde una perspectiva social y humanitaria, la investigación ofrece inteligencia espacial directamente aplicable a la protección civil. Al separar 
las zonas de combate directo de las áreas afectadas por ataques remotos, el modelo facilita la identificación de puntos críticos de desgaste. 
Esta objetividad analítica es vital para evaluar corredores de evacuación más seguros para civiles y optimizar la logística de las organizaciones de rescate en terreno.

La contribución metodológica radica en el diseño de un pipeline analítico reproducible para procesar datos geoespaciales de extrema volatilidad. 
Al aislar los datos por su naturaleza táctica (separar infantería de artillería) se optimiza el rendimiento del algoritmo K-Means, 
resolviendo el problema del ruido espacial que hace fracasar al análisis visual tradicional.

Finalmente, en el ámbito de la industria y el sector público, el proyecto demuestra cómo usar bases de datos masivas para herramientas de decisión estratégica. 
Este enfoque proporciona inteligencia accionable que es directamente escalable al análisis de riesgo geopolítico internacional, 
la consultoría de defensa y el periodismo de datos, entregando métricas precisas sobre la fluidez, escalada o estancamiento de un conflicto armado.
"""
)

centered_image("pages/photos/kmeans.png", width=620)
