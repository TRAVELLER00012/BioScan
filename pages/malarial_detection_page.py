import streamlit as st
from models.malarial_cells_model import run_detection, check_malaria_status
import pandas as pd


st.title("Malarial Detection")

st.subheader("Automated Malarial Infection Analysis")

col1, col2 = st.columns([2, 3])

with col1:
    st.image("./assets/cells2.jpg", width=500)
with col2:
    st.write("""
    <p style='font-size:1.125rem'>This module automates the detection of Plasmodium-infected cells from microscopic blood smear images using a Convolutional Neural Network (CNN)–based deep learning model. It differentiates between infected and uninfected red blood cells, providing a fast, scalable, and objective approach to malaria diagnosis. By integrating AI-driven image analysis, this project helps reduce the dependence on manual microscopic examination, which is often time-consuming and prone to human error.</p>
""", unsafe_allow_html=True)


with st.expander("How to Use", expanded=True):
    st.markdown("""
    ### 🧭 How to Use
    1. Upload **one or multiple microscopic blood smear images** using the uploader.  
    2. The model runs **automatically** upon upload — no need to click any button.  
    3. The system analyzes each image to detect malaria parasites.  
    4. Results are displayed visually in two graphs:
       - **Bar chart:** Shows the number of **Infected** vs **Uninfected** cells across the uploaded images.  
       - **Scatter plot:** Shows the **confidence score** for each image's prediction.  
    5. Infection ratio (**Infected / Total cells**) is calculated and displayed as a **percentage** along with a progress bar.  
    6. Finally, the **health status** of the sample is shown with a disclaimer: this model is for **educational purposes only** and does **not replace professional medical testing**.
    """)

with st.expander("How It Works", expanded=False):
    st.markdown("""
    ### ⚙️ Working of the Malarial Detection Model
    - The underlying **YOLO object detection model** has been trained to detect individual **parasitized (infected) and uninfected red blood cells** from microscopic blood smear images.  
    - Each image is normalized, resized, and passed through **YOLO’s detection layers** to identify cells and calculate confidence scores for each prediction.  
    - Predictions across all images are aggregated to compute the **infection ratio** and highlight potential malaria presence.  
    - Confidence scores provide insight into how certain the model is about each cell being infected or uninfected.
    """)

with st.expander("What to Expect", expanded=False):
    st.markdown("""
    ### 📊 Understanding the Results
    - The model outputs:
        - **Counts of infected and uninfected cells** in the sample(s).  
        - **Confidence score** for each prediction.  
        - **Infection ratio (%)** with a progress bar for a quick visual overview.  
        - **Health status** indicating the likelihood of malaria infection.  
    - Results are **for research and educational purposes only** and should **not replace professional medical testing**.  
    - Uploading **multiple images** provides a more representative analysis of the blood sample.  
    - In healthy samples, ideally **no infected cells** should be detected; in infected samples, the model highlights **parasitized cells clearly** with their confidence levels.
    """)


uploaded_files = st.file_uploader(
    "Choose a file", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

infected_count = 0
uninfected_count = 0
conf_rate = []
files = []
results = []

if len(uploaded_files) > 0:
    st.image(uploaded_files, width=300, caption=[
             file.name for file in uploaded_files])
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
    for file in uploaded_files:
        data, result = run_detection(file)
        infected_count += len(data["Infected"])
        uninfected_count += len(data["Uninfected"])
        conf_rate.append(data["Confidence_rate"])
        files.extend(data["File Name"])
        results.extend(result)


else:
    st.info(
        "Please upload one or more microscopic blood smear images for malarial detection.")

st.subheader("Detection Results", divider="blue")


if len(uploaded_files) > 0:

    st.bar_chart(pd.DataFrame([infected_count, uninfected_count], columns=[
                 'Count'], index=['Infected', 'UnInfected']))
    summary_df = pd.DataFrame({
        "File Name": files,
        "Confidence Rate": conf_rate
    })
    st.line_chart(data=summary_df, x="File Name", y="Confidence Rate")

    health_status, infection_percent, disclaimer = check_malaria_status(
        infected_count, uninfected_count)

    col1, col2 = st.columns([0.25, 0.75])
    with col1:
        st.markdown(
            f"**Infected Cells:** $\\frac{{{infected_count}}}{{{infected_count + uninfected_count}}} =$ "
            f"{infection_percent:.2f}%"
        )
    with col2:
        st.markdown("""
        <style>
        .stProgress .st-b8 .st-bm {
            background-color: tomato;
        }
        </style>
        """, unsafe_allow_html=True)
        st.progress(min(int(infection_percent), 100),
                    text="Infection %",)

    # Status with colored text
    if "Healthy" in health_status:
        st.success(f"**Status:** {health_status}")
    elif "Mild" in health_status:
        st.info(f"**Status:** {health_status}")
    elif "Moderate" in health_status:
        st.warning(f"**Status:** {health_status}")
    else:
        st.error(f"**Status:** {health_status}")

    # Disclaimer
    st.markdown(f"{disclaimer}")
else:
    st.warning("Please upload valid images with detectable blood cells.")
st.html(
    '''
    <style>
    hr {
        border-color: dodgerblue;
    }
    </style>
    <hr>
    '''
)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Previous Page", width="stretch"):
        st.switch_page("./pages/cells_detection_page.py")
with col2:
    if st.button("Next Page", width="stretch"):
        st.switch_page("./pages/breast_cancer_detection_page.py")
