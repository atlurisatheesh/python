import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv("tatkal_data.csv")

# Encode
df["class_type_num"] = df["class_type"].map({
    "sleeper": 1,
    "AC": 0
})

X = df[["class_type_num", "is_weekend"]]
y = df["confirmed"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "tatkal_model.pkl")

print("✅ Model trained and saved as tatkal_model.pkl")
