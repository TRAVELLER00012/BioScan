import streamlit as st

st.title("🧬 AI-Powered Blood Cell Analyzer")
st.write("### Revolutionizing Early Diagnosis through Artificial Intelligence")

# Optional Hero Image (you can replace with a relevant one)
# st.image("assets/ai_microscope_banner.jpg", use_column_width=True)

st.markdown("""
---
### 🌍 Project Overview
This project is an **AI-driven diagnostic assistant** that leverages **computer vision and deep learning** to analyze microscopic blood images and provide **automated health insights**.  
By detecting and classifying **Red Blood Cells (RBCs)** and **White Blood Cells (WBCs)**, our system can help in the **early detection of blood-related disorders** and **infection indicators** — all from simple image uploads.

---
### 🎯 Our Aim
The goal of this project is to make **medical image analysis faster, smarter, and more accessible**.  
Traditional microscopy requires expert supervision and time-consuming manual counting.  
With our model, users can simply **upload images of blood samples**, and the system will:
- Detect individual cells automatically  
- Count RBCs and WBCs precisely  
- Analyze their ratio to indicate possible abnormalities  
- Provide **data-backed health insights** for medical or research use

---
### ⚙️ How It Works
1. **Upload Sample Images:** Users upload one or more microscope images of blood samples.  
2. **AI Detection:** A trained deep learning model (powered by YOLOv8) detects and classifies each cell.  
3. **Automated Analysis:** The system aggregates counts, computes cell ratios, and gives a realistic diagnostic interpretation.  
4. **Insight Generation:** Results are displayed visually and numerically, helping users identify potential imbalances instantly.

---
### 💡 What Problems This Solves
- ✅ Eliminates **manual counting errors**
- ✅ Speeds up **diagnostic workflows**
- ✅ Makes **blood analysis accessible** in low-resource areas
- ✅ Offers a **learning platform** for students and researchers studying hematology and AI

---
### 🧠 Behind the Technology
- **Model Used:** YOLOv8-based detection model for RBC and WBC classification  
- **Frameworks:** Python, OpenCV, PyTorch, Streamlit  
- **Core Features:**
    - Multi-image processing  
    - Cell detection & ratio calculation  
    - Real-time visualization of results  
    - Health indicator summary  

---
### 🚀 Vision
We envision expanding this platform beyond blood samples — into a **multi-diagnostic AI platform** capable of detecting **malaria, anemia, and other cellular disorders** using the same unified pipeline.  
In the future, we aim to:
- Integrate **disease prediction** layers (e.g., malaria detection)  
- Build a **mobile-ready version** for rapid testing  
- Link with **IoT-based microscope devices** for automated data collection

---
### 👩‍🔬 In Summary
This project stands at the intersection of **healthcare and artificial intelligence**.  
It represents how a student-built AI tool can contribute toward a **faster, smarter, and more accessible medical future**.
""")

st.info("💡 Try it out! Navigate to the **Detection** page to upload sample images and see the AI in action.")


col1, col2, col3 = st.columns([2, 10, 1.05])
with col3:
    if st.button("Next Page"):
        st.switch_page("./pages/cells_detection_page.py")
