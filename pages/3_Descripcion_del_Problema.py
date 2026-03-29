import streamlit as st
from pages.utils.ui_theme import setup_page

setup_page("Descripción del Problema")

st.title("Descripción del Problema")

st.markdown(
    """
El problema central de esta investigación radica en la sobrecarga de datos geoespaciales que generan los conflictos modernos y la 
dificultad de interpretarlos de manera objetiva y verificar su autenticidad. Al extraer miles de incidentes de plataformas abiertas, 
el análisis visual tradicional colapsa, ya que el ojo humano es incapaz de agrupar coordenadas masivas sin caer en sesgos cognitivos o agrupar puntos por simple proximidad visual.

A esto se suma una brecha analítica importante: tratar todos los incidentes violentos como un fenómeno único. Mezclar en un mismo mapa los 
combates de trincheras (infantería) con los ataques de misiles a larga distancia (artillería) distorsiona la realidad táctica y arrastra los frentes de 
batalla fuera de su posición real.

Por lo tanto, los problemas científicos a resolver con la investigación son los siguientes:

1. Validar la veracidad empírica (Niebla de Guerra): Superar la desinformación y el ruido estadístico (Fake News/Propaganda) de los conflictos modernos, 
garantizando que el modelo algorítmico se alimente exclusivamente de incidentes verificados y estructurados para evitar la ingesta de falsos positivos en el mapeo territorial.

2. Superar el sesgo visual: Utilizar cálculo matemático estricto (minimización de distancias) para agrupar las coordenadas sin 
intervención humana en un frente de más de 1.000 kilómetros.

3. Segmentar la realidad táctica: Identificar de forma independiente dónde se concentra la línea de contacto (guerra terrestre) y 
dónde ocurren los patrones de ataque en la retaguardia (guerra aérea).
"""
)

st.markdown("<div style='height: 3.2rem;'></div>", unsafe_allow_html=True)

left, center, right = st.columns([1, 3, 1])
with center:
    st.image("pages/photos/UKR3.png", width=980)
