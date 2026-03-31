import streamlit as st
from pathlib import Path

import pandas as pd
from pages.utils.ui_theme import setup_page

setup_page("Estrategia de Búsqueda y Uso de IA")

st.title("Estrategia de Búsqueda y Uso de IA")

left_col, right_col = st.columns([1.45, 1], gap="large", vertical_alignment="center")

with left_col:
    st.subheader("Lista manual inicial de palabras clave")
    st.markdown(
        """
- clustering
- algoritmo K-Means
- análisis geoespacial
- dataset de conflictos
- dataset guerra de Ucrania
- análisis táctico en Ucrania
"""
    )

with right_col:
    pad_left, image_col, pad_right = st.columns([0.2, 1, 0.2])
    with image_col:
        st.image("pages/photos/gemini.png", width="stretch")

st.subheader("Prompt usado")
st.code(
    'Ayúdame a recopilar información o a encontrar dataset en base a las siguientes palabras clave para un proyecto '
    'sobre segmentación espacial para la guerra de Ucrania: [clustering, '
    'algoritmo de K-Means , análisis geoespacial, dataset de conflictos, aprendizaje no supervisado, '
    'análisis táctico en Ucrania,dataset guerra de Ucrania, dinamica del frente]. Dame términos técnicos, variantes usadas '
    'en papers o paginas que recopilan informacion y como más importante dataset de fuentes confiables y de fácil descarga.',
    language="text",
)


st.subheader("Expansión con IA")
st.markdown(
    """
- Analisis de patrones de puntos 
- ACLED(Armed Conflict Location & Event Data Project)
- Geolocation Intelligence (GEOINT)
- Clustering espacial basado en densidad
- UCDP
- DBSCAN
- Warfare Informatics
- Aprendizaje no supervisado
"""
)

st.subheader("Validación humana")
st.markdown(
    """
Clustering es el concepto teórico correcto para agrupar coordenadas masivas sin sesgo visual. 
Al investigar algoritmos espaciales, se validó que tanto K-Means como DBSCAN son viables para datos geoespaciales, 
ya que agrupan por cercanía matemática y densidad. Esto permite evaluar metodológicamente cuál de los dos segmenta mejor el mapa en zonas tácticas operativas.

Al revisar UCDP (Uppsala Conflict Data Program) se encontro que es la fuente de referencia para la ONU para este tipo de conflictosy es de libre acceso, pero 
presenta el problema de que sus datos se actualizan más lento y omiten incidentes menores de infantería, lo cual es perjudicial para mapear una guerra de trincheras.

El término ACLED (Armed Conflict Location & Event Data Project) corresponde a una organización que funciona como un 
observatorio de crisis a nivel mundial. Se validó como la fuente empírica más robusta para este proyecto, superando a UCDP por su mayor cantidad de datos. 
Sin embargo, fue requerido solicitar acceso nivel Research (Investigador) mediante correo para uso académico, una restricción de seguridad que la IA 
omitió inicialmente al asegurar que los datos eran de descarga libre.

Durante la exploración técnica de la API de ACLED, se identificó una restricción, el acceso a las coordenadas exactas 
tiene un embargo de 12 meses para las cuentas de investigador. Por lo tanto, de usarse este datsetet sera en una ventana de tiempo anterior a marzo de 2025.

Además, se descartaron términos de búsqueda muy generales como "aprendizaje no supervisado" en favor de conceptos precisos como "Análisis de Patrones de Puntos" y 
"Clustering Espacial".

Para la investigación de información, estructuración teórica, correciones de texto y validación metodológica se utilizó Gemini 3.1 Pro, y para el código de la app de streamlit se 
utilizó GitHub Copilot con el modelo GPT-5.3-Codex.
"""
)

final_left, final_right = st.columns([1.35, 1], gap="large", vertical_alignment="top")

with final_left:
    st.subheader("Construcción final de terminos clave")
    st.markdown(
        """
- Spatial Clustering(Agrupamiento Espacial)
- K-Means
- DBSCAN
- Análisis de Patrones de Puntos
- GEOINT (Geospatial Intelligence)
- Armed conflict data
- ACLED
- Dinámicas de la Línea de Frente
"""
    )

with final_right:
    st.markdown("<div style='height: 2.3rem;'></div>", unsafe_allow_html=True)
    pad_left, image_col, pad_right = st.columns([0.1, 1, 0.1])
    with image_col:
        st.image("pages/photos/github.png", width=520)


@st.cache_data
def load_acled_data(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)


csv_path = Path(__file__).resolve().parents[1] / "data" / "acled_ukraine_oct2024_jan2025.csv"

st.markdown(
    """
<hr style="border: 0; border-top: 1px solid rgba(201, 220, 236, 0.35); margin: 2.2rem 0 1.3rem 0;" />
""",
    unsafe_allow_html=True,
)

table_left, table_center, table_right = st.columns([0.08, 1, 0.08])
with table_center:
    st.subheader("Tabla del CSV obtenido desde ACLED")
    if csv_path.exists():
        df_acled = load_acled_data(csv_path)
        with st.expander("Ver/ocultar tabla del CSV", expanded=False):
            st.dataframe(df_acled, width="stretch", height=430)
    else:
        st.warning("No se encontró el archivo CSV en la carpeta data.")
