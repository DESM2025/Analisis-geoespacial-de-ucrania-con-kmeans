import streamlit as st
from pages.utils.ui_theme import setup_page

setup_page("Analisis espacial del conflicto en Ucrania mediante clustering geoespacial")

st.title("Analisis espacial del conflicto en Ucrania mediante clustering geoespacial")

st.markdown("<div style='height: 18vh;'></div>", unsafe_allow_html=True)

left, right = st.columns([1.1, 1], gap="large")

with left:
    st.markdown(
    """
El objetivo de la investigación será comprender y cartografiar la dinámica territorial de un conflicto real como el de Ucrania.

Para lograr esto la investigación se apoyará en la IA y algoritmos como herramientas de analítica de los datos recopilados, específicamente se espera usar 
algoritmos de clustering geoespacial (como K-Means y DBSCAN), para procesar miles de coordenadas geográficas exactas de incidentes. En lugar de tratar estos incidentes como un conjunto 
homogéneo se propone una aproximación metodológica estratégica, al separar los enfrentamientos directos de infantería de los ataques remotos y bombardeos.

Al aplicar estos modelos de aprendizaje no supervisado sobre las coordenadas geográficas exactas de miles de incidentes extraídos de las bases de datos a investigar, 
el algoritmo debería poder agrupar estos eventos espaciales y permitir visualizar y comparar, libres de sesgo humano, 
las distintas lógicas territoriales que rigen la guerra moderna.
"""
)

with right:
    st.markdown("<div style='margin-top: -1vh;'></div>", unsafe_allow_html=True)
    st.image("pages/photos/UKR4.png", width=1500)
