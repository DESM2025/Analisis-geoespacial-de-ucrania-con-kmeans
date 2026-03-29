import streamlit as st
from pages.utils.ui_theme import centered_image, setup_page

setup_page("Fundamento o Motivación")

st.title("Fundamento o Motivación")

st.markdown(
    """
La motivación de esta investigación surge de la necesidad de aportar objetividad analítica al estudio de los conflictos armados modernos. Pues históricamente 
la informacion de frentes de batalla ha dependido de reportes cualitativos, narrativas de medios de comunicación o mapas trazados manualmente, 
los cuales son susceptibles al sesgo humano o a la asimetría de la información y a la niebla informativa en una guerra.

Gracias a la tecnologia y conectividad que existe actualmente, hay una grand disponibilidad de bases de datos estructuradas y de alta granularidad, 
como ACLED, lo que permite que exista una oportunidad para abordar estos fenómenos territoriales directamente desde la Ciencia de Datos.

El fundamento principal de la investigación se separa en dos apartados:

Metodología: Demostrar que los algoritmos de aprendizaje no supervisado pueden procesar miles de coordenadas aisladas para revelar patrones tácticos subyacentes. 
Permitiendo trascender el análisis cualitativo tradicional, ofreciendo en su lugar un modelo de agrupamiento matemático, replicable y libre de sesgos interpretativos.

Aplicación: Construir una investigación rigurosa que resuelva un problema espacial del mundo real, utilizando técnicas computacionales para transformar 
un volumen masivo de datos crudos en inteligencia geoespacial útil para la Geografía y las Ciencias Políticas.
"""
)

st.markdown("<div style='height: 4.5rem;'></div>", unsafe_allow_html=True)
centered_image("pages/photos/ACLED.png", width=680)
