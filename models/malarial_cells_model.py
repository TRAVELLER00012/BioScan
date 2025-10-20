import os
from ultralytics import YOLO
import tempfile

model = YOLO("../scripts/runs/detect/train2/weights/best.pt")
model.to("cpu")


def run_detection(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name
        file_name = uploaded_file.name

    results = model.predict(temp_path)

    data = {
        "Infected": [],
        "Uninfected": [],
        "Confidence_rate": [],
        "File Name": []
    }

    for r in results:
        for box in r.boxes:
            detection_id = box.cls[0]
            conf_rate = box.conf[0].cpu().item()
            cell_type = "Infected" if detection_id == 0 else "Uninfected"

            if cell_type == "Infected":
                data["Infected"].append(file_name)
            else:
                data["Uninfected"].append(file_name)

            data["Confidence_rate"].append(conf_rate)
            data["File Name"].append(file_name)

    return data, results


def check_malaria_status(infected_count, uninfected_count):
    total_cells = infected_count + uninfected_count
    if total_cells == 0:
        return "No cells detected.", 0.0

    infection_ratio = infected_count / total_cells * 100

    if infection_ratio <= 1:
        status = "Healthy ✅"
    elif infection_ratio <= 5:
        status = "Mild / Monitor ⚠️"
    elif infection_ratio <= 20:
        status = "Moderate / Consult Doctor ⚠️"
    else:
        status = "Severe / Seek Medical Attention ❌"

    note = "ℹ️ **Disclaimer:** This is an AI-generated result for educational/demo purposes. "\
           "It does not replace real medical advice or diagnosis."

    return status, infection_ratio, note
