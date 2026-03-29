import streamlit as st
from pages.utils.ui_theme import setup_page

setup_page("Proyecto de Investigación")

st.title("Área OCDE")
left, right = st.columns([1.1, 1], gap="large", vertical_alignment="center")

with left:
    st.markdown(
        """
La idea central de esta investigación pertenece al dominio de las Ciencias Sociales, específicamente a las Ciencias Políticas y Geografía, ya que el problema fundamental a resolver 
con esta investigación es la comprensión y delimitación de las dinámicas territoriales y tácticas del conflicto en Ucrania de forma clara.

Para abordar este problema sociopolítico, el proyecto se apoya de forma en las Ciencias Naturales (Computación e Informática). 
Pues se planea utilizar el algoritmo K-Means, como una herramienta de cálculo avanzado para procesar el volumen de datos.

A nivel metodológico se trata de una investigación cuantitativa, exploratoria y descriptiva. Pues al delegar la segmentación territorial a un modelo de aprendizaje no supervisado 
se elimina el sesgo humano y se descubren patrones espaciales objetivos basados estrictamente en los datos recopilados en la investigación.
"""
    )

with right:
    st.image("pages/photos/OECD.png", width=560)