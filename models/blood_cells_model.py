from ultralytics import YOLO
import tempfile

model = YOLO("runs/detect/train5/weights/best.pt")


def run_detection(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name

    results = model.predict(temp_path)

    rbc_count = 0
    wbc_count = 0
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            if cls_id == 0:
                rbc_count += 1
            elif cls_id == 1:
                wbc_count += 1
    if wbc_count == 0:
        ratio = float('inf')
    else:
        ratio = rbc_count / wbc_count
    return results, rbc_count, wbc_count, ratio


def check_ratio(ratio):
    if 4 <= ratio <= 10:
        status = "RBC/WBC ratio is within normal range. Sample shows a healthy distribution of blood cells."
    elif ratio < 4:
        status = "Detected relatively fewer RBCs compared to WBCs. Possible anemia or low RBC count."
    else:
        status = "Detected relatively high RBCs compared to WBCs. Sample seems within safe range, but verify with more images."

    return status
