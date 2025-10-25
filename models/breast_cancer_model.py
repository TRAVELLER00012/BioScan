import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from ultralytics import YOLO
import tempfile
import tensorflow as tf

model = YOLO("../scripts/runs/segment/train2/weights/best.pt")
scaler = StandardScaler()
data = pd.read_csv("dataset/breast-cancer.csv")
X = data.iloc[:, 2:].values
scaler.fit(X)


def run_detection(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name
        file_name = uploaded_file.name

    results = model.predict(temp_path)

    benign = []
    malignant = []
    conf = []
    for r in results:
        for box in r.boxes:
            c_id = int(box.cls[0])
            c = round(float(box.conf[0]), 4)
            if c_id == 1:
                benign.append(c_id)
                conf.append(c)
            if c_id == 2:
                malignant.append(c_id)
                conf.append(c)

    return file_name, conf, benign, malignant


def run_classification(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst):
    ann = tf.keras.models.load_model("scripts/breast_cancer.keras")
    return ann.predict(scaler.transform(np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                                                  compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]).reshape(1, -1)))


def run_classification(data):
    ann = tf.keras.models.load_model("scripts/breast_cancer.keras")
    return int(ann.predict(scaler.transform(np.array(data).reshape(1, -1))) > 0.5)

# M -> 1
# B -> 0
