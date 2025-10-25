import streamlit as st
import pandas as pd
import numpy as np
from models.breast_cancer_model import run_detection, run_classification

st.title("Breast Cancer Detection")

st.subheader("AI-Powered Breast Cancer Diagnosis System")

col1, col2 = st.columns([2, 3])

with col1:
    st.image("./assets/breast_cancer.jpg", width=500)
with col2:
    st.write("""
    <p style='font-size:1.125rem'>
    This platform integrates both <b>image-based</b> and <b>data-based</b> artificial intelligence models to analyze breast cancer risk.
    Using a <b>YOLOv8s segmentation model</b> for ultrasound imaging and an <b>Artificial Neural Network (ANN)</b> for numerical feature prediction,
    it helps classify cases as <b>Benign</b> or <b>Malignant</b> based on both imaging and diagnostic parameters.
    </p>
    """, unsafe_allow_html=True)

with st.expander("How to Use", expanded=True):
    st.markdown("""
    ### 🧭 How to Use
    1. Upload one or more **breast ultrasound scans** using the uploader below. The AI model will automatically process each image to identify and segment potential tumor regions.
    2. Observe the **segmented output**, where the system highlights areas of interest such as *Benign*, *Malignant*, or *Normal* tissue regions. Each region is color-coded and labeled for easy visual understanding.
    3. For cases where you also have **numerical diagnostic data** — such as cell radius, perimeter, concavity, and smoothness — you can input these values in the **data table**.
       The **Artificial Neural Network (ANN)** will analyze them to predict tumor type based on learned medical patterns.
    4. The results from both models — image-based and data-based — can be compared to observe **agreement or variation** between visual and numerical diagnostics.
    5. All results, visualizations, and predictions are provided strictly for **research, education, and awareness purposes**.
       This platform is **not a replacement for professional medical diagnosis**.
    """)


with st.expander("How It Works", expanded=False):
    st.markdown("""
    ### ⚙️ Model Workflow
    #### 🧩 YOLOv8m Segmentation Model
    - The **YOLOv8m-seg model** is a convolutional neural network trained specifically on labeled breast ultrasound images.
      It performs **object detection and instance segmentation** simultaneously, allowing it to both locate and classify tumor regions.
    - Each prediction includes a **bounding area**, a **segmentation mask**, and a **confidence score** representing how sure the model is about its detection.
    - The model categorizes visible tissue regions into:
        - 🟢 **Normal:** Healthy tissue patterns with no suspicious growths detected.
        - 🟡 **Benign:** Non-cancerous tissue growth or cystic structures.
        - 🔴 **Malignant:** Suspicious or cancerous regions that require further professional evaluation.

    #### 🧠 Artificial Neural Network (ANN)
    - The ANN is a **fully connected feed-forward neural network** designed for tabular diagnostic data.
      It analyzes features such as:
        - Mean radius, texture, perimeter, area, smoothness
        - Compactness, concavity, symmetry, fractal dimension, etc.
    - The model outputs a **binary classification**:
        - `1 → Malignant`
        - `0 → Benign`
    - By using both visual and numerical analysis, the system offers **cross-verification** and a more holistic view of diagnostic outcomes.
    """)


with st.expander("What to Expect", expanded=False):
    st.markdown("""
    ### 📊 Understanding the Results
    - Once you upload an image, the **Image Model** will generate a detailed visualization highlighting each detected region.
      The segmented areas are color-coded and labeled with their predicted categories and confidence levels.
    - The **category summary table** shows the count and confidence of each prediction type — helping you quickly assess the dominant tissue class in the scan.
    - If you’ve used the **ANN-based model**, it will display a **numerical prediction result**, indicating whether the features represent a *Benign* or *Malignant* tumor.
    - These combined insights provide:
        - A clear understanding of **how AI interprets tissue patterns**
        - A chance to **compare visual and numerical diagnostics**
        - Awareness of **AI-assisted screening potential** in early cancer detection
    - ⚠️ Please remember:
      This platform is intended solely for **educational and research demonstrations**.
      The predictions **must not be used for medical treatment or diagnostic decisions**.
    """)


st.header("📤 Upload Breast Ultrasound Images")
uploaded_files = st.file_uploader(
    "Choose a file", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

file_names = []
malignant_count = 0
benign_count = 0
net_conf = []

if len(uploaded_files) > 0:
    st.image(uploaded_files, width=275, caption=[
             file.name for file in uploaded_files])
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
    for file in uploaded_files:
        file_name, conf, benign, malignant = run_detection(file)
        file_names.append(file_name)
        benign_count += len(benign)
        malignant_count += len(malignant)
        net_conf.append(conf)
else:
    st.info("Please upload one or more breast ultrasound images for AI-based analysis.")

st.subheader("Detection Results", divider="blue")
if len(uploaded_files) > 0:
    st.bar_chart(pd.DataFrame([benign_count, malignant_count], columns=[
                 'Count'], index=['Benign', 'Malignant']))
    summary_df = pd.DataFrame({"Image": file_names, "Confidence": net_conf})
    st.line_chart(summary_df, x="Image", y="Confidence")
else:
    st.warning(
        "Please upload valid breast ultrasound images with detectable tissue regions.")

st.header("🧮 Text-Based Prediction")
st.markdown(
    "Enter diagnostic data below to predict tumor type:")

with st.form("ann_input_form"):
    cols = st.columns(3)
    input_fields = [
        "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
        "compactness_mean", "concavity_mean", "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",
        "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se",
        "compactness_se", "concavity_se", "concave_points_se", "symmetry_se", "fractal_dimension_se",
        "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
        "compactness_worst", "concavity_worst", "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
    ]

    input_values = {}
    for i, field in enumerate(input_fields):
        with cols[i % 3]:
            input_values[field] = st.number_input(field.replace(
                "_", " ").capitalize(), step=0.001, format="%.5f")

    submitted = st.form_submit_button("Predict Tumor Type")
    if submitted:
        st.write("✅ Form submitted!")
        input_array = np.array([input_values[field] for field in input_fields])
        result = run_classification(input_array)
        if result == 1:
            st.error("🔴 Predicted Tumor Type: Malignant")
            st.warning(
                "⚠️ Immediate medical consultation is recommended. This prediction is AI-based and for educational purposes only.")
        else:
            st.info("🟢 Predicted Tumor Type: Benign")
            st.warning(
                "⚠️ Although classified as Benign, it is not guaranteed to be completely safe. Regular checkups and professional assessment are advised.")


st.markdown("""
> ⚠️ **Disclaimer:**  
> This system is for **educational and research purposes only**.  
> It is **not a substitute for professional medical advice** or clinical diagnosis.
""")

st.html('''
<style>
hr {
    border-color: dodgerblue;
}
</style>
<hr>
''')

if st.button("Previous Page"):
    st.switch_page("./pages/malarial_detection_page.py")
