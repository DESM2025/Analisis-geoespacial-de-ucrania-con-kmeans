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
- aprendizaje no supervisado
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
    'sobre segmentación espacial con K-Means para la guerra de Ucrania: [clustering, '
    'algoritmo de K-Means , análisis geoespacial, dataset de conflictos, aprendizaje no supervisado, '
    'análisis táctico en Ucrania,dataset guerra de Ucrania, dinamica del frente]. Dame términos técnicos, variantes usadas '
    'en papers o paginas que recopilan informacion y como más importante dataset de fuentes confiables y de fácil descarga.',
    language="text",
)

st.subheader("Expansión con IA")
st.markdown(
    """
- Analisis de patrondes de puntos 
- ACLED(Armed Conflict Location & Event Data Project)
- Geolocation Intelligence (GEOINT)
- Clustering espacial basado en densidad
- UCDP
- Warfare Informatics
"""
)

st.subheader("Validación humana")
st.markdown(
    """
Se comprobo que "clustering" es el concepto teorico correcto para agrupar coordenadas masivas sin sesgo visual. Sobre K-Means, 
se valido al buscar casos similares que puede ser utilizado para datos geoespaciales porque agrupa por cercania matematica, 
lo que en teoria resuelve perfectamente el problema de segmentar el mapa en zonas tacticas

Al revisar UCDP(Uppsala Conflict Data Program) se comprobo que es la fuente de referencia para la ONU y es de 
libre acceso pero tiene el problema de que sus datos se actualizan mas lento y omiten incidentes menores.

El término ACLED que mencionó la IA es el Armed Conflict Location & Event Data
Project, una organización que funciona como un observatorio de crisis y documenta
incidentes de violencia política a nivel mundial. Se validó como la fuente más robusta sobre UCDP pero 
fue requerido solicitar un acceso a nivel Research (Investigador) para uso académico mediante correo, 
cosa que la ia no menciono y esta aseguraba que no era necesario para obtener los datos.

Durante la investigación se identificó una restricción metodológica de la plataforma pues el
acceso a los datos de coordenadas exactas tiene un embargo para los últimos
12 meses para las cuentas de investigador. Por lo tanto, el proyecto de llevarse a cabo debera aplicarse sobre
una ventana temporal específica y consolidada del conflicto (desde antes de marzo de 2025).

Además, se descartaron términos muy generales como aprendizaje no supervisado en favor de
análisis de Patrones de Puntos para enfocar la búsqueda exacta.

Para la investigación de informacion se utilizó Gemini Pro 3.1, y para la parte de código de la pagina 
se utilizó GitHub Copilot con el modelo GPT-5.3-Codex.
"""
)

final_left, final_right = st.columns([1.35, 1], gap="large", vertical_alignment="top")

with final_left:
    st.subheader("Construcción final de terminos clave")
    st.markdown(
        """
- Spatial Clustering(Agrupamiento Espacial)
- K-Means
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
