import streamlit as st


def setup_page(title: str) -> None:
    st.set_page_config(page_title=title, page_icon="🌍", layout="wide")
    apply_theme()
    add_sidebar_footer()


def apply_theme() -> None:
    st.markdown(
        """
<style>
    .stApp {
        background: linear-gradient(180deg, #0f2233 0%, #17324a 45%, #1f425f 100%);
        color: #e9f1f8;
    }

    [data-testid="stAppViewContainer"] {
        color: #e9f1f8;
    }

    h1, h2, h3 {
        color: #f7fbff;
    }

    section.main .block-container {
        font-size: 1.18rem !important;
    }

    section.main .block-container h1 {
        font-size: 3.35rem !important;
        line-height: 1.12 !important;
    }

    section.main .block-container h2 {
        font-size: 2.35rem !important;
        line-height: 1.18 !important;
    }

    section.main .block-container h3 {
        font-size: 1.8rem !important;
        line-height: 1.2 !important;
    }

    section.main .block-container p,
    section.main .block-container li,
    section.main .block-container label,
    section.main .block-container [data-testid="stMarkdownContainer"] p,
    section.main .block-container [data-testid="stMarkdownContainer"] li {
        color: #e9f1f8;
        font-size: 1.22rem !important;
        line-height: 1.68 !important;
    }

    div[data-testid="stAlert"] {
        background-color: rgba(25, 58, 84, 0.6);
        border: 1px solid rgba(180, 210, 235, 0.25);
    }

    section[data-testid="stSidebar"] {
        background: #0b1d2d;
        border-right: 1px solid rgba(180, 210, 235, 0.15);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }

    .sidebar-spacer {
        flex: 1;
    }

    .sidebar-footer {
        margin-top: 0.75rem;
        padding-top: 0.75rem;
        border-top: 1px solid rgba(180, 210, 235, 0.25);
        font-size: 0.76rem;
        line-height: 1.35;
        color: #c7d6e4;
    }

    /* Reetiqueta visualmente la entrada principal "app" como "Idea planteada" */
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] ul li:first-child [data-testid="stMarkdownContainer"] p {
        font-size: 0;
        position: relative;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] ul li:first-child [data-testid="stMarkdownContainer"] p::after {
        content: "Idea planteada";
        font-size: 1.05rem;
        font-weight: 600;
        color: #e9f1f8;
    }
</style>
""",
        unsafe_allow_html=True,
    )


def add_sidebar_footer() -> None:
    with st.sidebar:
        st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)
        st.markdown(
            """
<div class="sidebar-footer">
    Diego Silva Madariaga<br>
    Metodología de investigación en ciencia de datos<br>
    Universidad Tecnológica Metropolitana
</div>
""",
            unsafe_allow_html=True,
        )


def centered_image(image_path: str, width: int = 500) -> None:
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.image(image_path, width=width)
