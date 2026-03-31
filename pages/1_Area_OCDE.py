import streamlit as st
from pages.utils.ui_theme import setup_page

setup_page("Proyecto de Investigación")

st.title("Área OCDE y Objetivos de Desarrollo Sostenible")
left, right = st.columns([1.1, 1], gap="large", vertical_alignment="center")

with left:
    st.markdown(
    """
La idea central de esta investigación se enmarca en el dominio de las Ciencias Sociales, específicamente en el área de la Geografía. 
Ya que el problema fundamental a resolver es la comprensión y delimitación espacial de las dinámicas territoriales del conflicto en Ucrania, analizando cómo se 
transforma el territorio a lo largo del tiempo.

El proyecto se alinea con dos Objetivos de Desarrollo Sostenible (ODS). 

- ODS 16 Paz, justicia e instituciones sólidas, al aportar inteligencia geoespacial empírica para mapear objetivamente la violencia.

- ODS 11 Ciudades y comunidades sostenibles, ya que al separar 
matemáticamente el combate de infantería de los bombardeos remotos sobre áreas urbanas, el modelo facilita la identificación de zonas de riesgo y corredores de evacuación 
más seguros para la protección civil.

Esta sera una investigación cuantitativa y exploratoria. Para procesar el masivo volumen de coordenadas, el proyecto utilizara algoritmos 
de clustering espacial. Al delegar la segmentación territorial a modelos de aprendizaje no supervisado, se elimina el sesgo visual humano y se descubren patrones espaciales objetivos basados estrictamente en los datos.
"""
)

with right:
    st.image("pages/photos/OECD.png", width=560)

    