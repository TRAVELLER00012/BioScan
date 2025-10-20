import streamlit as st

st.set_page_config(layout="wide", page_title="Bio Scan", page_icon="🧬")


pg = st.navigation(
    [
        st.Page("./pages/homepage.py", title="Home"),
        st.Page("./pages/cells_detection_page.py", title="Cells Detection"),
        st.Page("./pages/malarial_detection_page.py",
                title="Malarial Detection")
    ],
    position="sidebar"
)
pg.run()
