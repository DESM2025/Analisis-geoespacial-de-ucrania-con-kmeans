import streamlit as st
from pages.utils.ui_theme import setup_page

setup_page("Análisis espacial del conflicto en Ucrania mediante clustering geoespacial con el algoritmo K-Means")

st.title("Análisis espacial del conflicto en Ucrania mediante clustering geoespacial con el algoritmo K-Means")

st.markdown("<div style='height: 18vh;'></div>", unsafe_allow_html=True)

left, right = st.columns([1.1, 1], gap="large")

with left:
    st.markdown(
        """
El objetivo de la investigación sera comprender y cartografiar la dinámica territorial de un conflicto real como el de Ucrania durante el periodo de tiempo de la 
campaña de invierno (1 de octubre de 2024 a 31 de enero de 2025).

Para lograr este objetivo la investigación se apoyara en la Inteligencia Artificial como herramienta analítica de los datos recopilados, específicamente del 
algoritmo k-means, para procesar miles de coordenadas geográficas exactas de incidentes.En lugar de tratar estos incidentes como un conjunto homogéneo se propone una 
aproximación metodológica estrategica, al separar los enfrentamientos directos de infantería de los ataques remotos y bombardeos.

Al aplicar el algoritmo K-Means sobre las coordenadas geográficas exactas de miles de incidentes extraídos de las bases de datos de a investigar, 
el modelo deberia poder agrupa estos eventos espaciales y como permitir visualizar y comparar libres de sesgo humano, 
las distintas lógicas territoriales que rigen la guerra terrestre frente a la guerra actual.
"""
    )

with right:
    st.markdown("<div style='margin-top: -1vh;'></div>", unsafe_allow_html=True)
    st.image("pages/photos/UKR4.png", width=1500)
