import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "tatkal_model.pkl")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("ML model file not found")

model = joblib.load(MODEL_PATH)


def predict_confirmation(class_type: str, is_weekend):
    class_num = 1 if class_type == "sleeper" else 0
    weekend_num = 1 if is_weekend else 0

    probability = model.predict_proba([[class_num, weekend_num]])[0][1]
    return float(round(probability * 100, 2))
