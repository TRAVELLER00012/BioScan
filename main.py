import streamlit as st

st.set_page_config(layout="wide", page_title="Bio Scan", page_icon="🧬")


pg = st.navigation({
    "BioScan": [
        st.Page("./pages/homepage.py", title="Home"),
    ],
    "Cells":    [
        st.Page("./pages/cells_detection_page.py", title="Cells Detection"),
        st.Page("./pages/malarial_detection_page.py",
                title="Malarial Detection")
    ],
    "Cancer": [
        st.Page("./pages/breast_cancer_detection_page.py",
                title="Breast Cancer Detection")
    ]
},
    position="sidebar"
)
pg.run()
