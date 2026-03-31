import streamlit as st
from pages.utils.ui_theme import centered_image, setup_page

setup_page("Fundamento o Motivación")

st.title("Fundamento o Motivación")

st.markdown(
    """
La motivación de esta investigación surge de la necesidad de aportar objetividad analítica al estudio de los conflictos armados modernos. 
Ya que historicamente la información de los frentes de batalla ha dependido de reportes cualitativos, narrativas de medios de comunicación o mapas trazados manualmente, 
los cuales son susceptibles al sesgo visual y humano, la asimetría de la información y la niebla de guerra.

Gracias a la tecnología y conectividad actual, existe una gran disponibilidad de bases de datos estructuradas y de alta calidad, como ACLED. Esto abre una oportunidad 
para abordar estos fenómenos territoriales directamente desde la Ciencia de Datos.

Es por esto que el fundamento principal de la investigación se divide en dos partes:

- Metodología: Evaluar y comparar empíricamente qué algoritmo de clustering espacial (como K-Means o DBSCAN) se adapta mejor al objetivo de cartografiar las zonas operativas. 
buscando determinar qué modelo matemáticosegmenta el territorio de la forma más fiel a la realidad táctica y libre de sesgos interpretativos.

- Aplicación: Construir una investigación que resuelva un problema espacial real y actual, utilizando estas técnicas computacionales para transformar un volumen 
masivo de datos crudos en inteligencia geoespacial (GEOINT) directamente útil para la Geografía y la planificación territorial.
"""
)
st.markdown("<div style='height: 4.5rem;'></div>", unsafe_allow_html=True)
centered_image("pages/photos/ACLED.png", width=680)
