import streamlit as st

st.set_page_config(page_title="AI-Powered Medical Analyzer",
                   page_icon="🧬", layout="wide")

st.title("🧬 AI-Powered Medical Analyzer")
st.write("### Revolutionizing Early Diagnosis through Artificial Intelligence")

st.markdown("""
---
### 🌍 Project Overview
Welcome to the **AI-Powered Medical Analyzer**, an advanced, multi-diagnostic platform built to assist in **medical image analysis using deep learning**.  
Our system uses computer vision to automatically detect patterns in medical images — helping identify diseases such as **blood disorders, malaria, and breast cancer** with accuracy and speed.

By leveraging **state-of-the-art YOLOv8 segmentation and classification models**, the platform aims to make diagnostics:
- Faster  
- More accessible  
- Less dependent on manual microscopy  

---

### 🧩 Available Modules

#### 🔬 **1. Blood Cell Detection**
- Detects and classifies **Red Blood Cells (RBCs)** and **White Blood Cells (WBCs)**  
- Computes ratios and abnormalities  
- Useful for identifying potential **anemia or infection indicators**  

🧠 **How it Works:**
Upload your microscopic blood images, and the AI automatically identifies and counts RBCs and WBCs using **YOLOv8-based object detection**.

---

#### 🦠 **2. Malarial Cell Detection**
- Detects **infected vs. uninfected blood cells**
- Helps in **early malaria diagnosis**
- Uses **CNN-based feature extraction** for precise identification

💡 **Usage:**
Upload blood smear images, and the AI highlights infected cells and gives a percentage of infection spread.

---

#### 🎗️ **3. Breast Cancer Cell Detection**
- Classifies images as **Normal**, **Benign**, or **Malignant**
- Uses **YOLOv8s segmentation** to identify cancerous tissue regions  
- Generates a chart showing the proportion of each type in your dataset  

📘 **Definitions:**
- **Normal:** Healthy breast tissue cells  
- **Benign:** Non-cancerous, but possibly abnormal cell growth  
- **Malignant:** Cancerous cells that can spread and require medical attention  

⚠️ **Disclaimer:**  
This module is **AI-generated and research-based**, and does **not replace professional medical diagnosis**.  
It is meant for **educational and experimental** purposes only.

---

### ⚙️ Under the Hood
- **Core Models:** YOLOv8, CNN-based classifiers  
- **Frameworks:** PyTorch, OpenCV, Streamlit  
- **Pipeline:**
  1. Upload → 2. AI Detection → 3. Visualization → 4. Statistical Report  

---

### 🚀 Vision
This project represents a step toward a **unified AI diagnostic system**, enabling:
- Multi-disease detection from a single interface  
- Integration with **IoT microscope devices**  
- Support for **mobile and offline analysis**

---

### 👩‍🔬 In Summary
The **AI-Powered Medical Analyzer** is a research initiative combining:
- Biomedical imaging  
- Artificial intelligence  
- Modern web technologies  

It’s a student-built effort to **bridge technology and healthcare** — showing how AI can empower doctors, students, and researchers alike.
""")

st.info("💡 Try any module below to experience AI-assisted medical image detection.")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🩸 Blood Cell Detection", use_container_width=True):
        st.switch_page("./pages/cells_detection_page.py")
with col2:
    if st.button("🦠 Malarial Detection", use_container_width=True):
        st.switch_page("./pages/malarial_detection_page.py")
with col3:
    if st.button("🎗️ Breast Cancer Detection", use_container_width=True):
        st.switch_page("./pages/breast_cancer_detection_page.py")
