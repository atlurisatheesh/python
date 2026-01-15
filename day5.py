import pandas as pd

df = pd.read_csv("tatkal_data.csv")
print(df)
print(df.head())     # First 5 rows
print(df.columns)   # Column names
print(df.shape)     # (rows, columns)


sleeper_df = df[df["class_type"] == "sleeper"]
print(sleeper_df)

weekend_df = df[df["is_weekend"] == 1]
print(weekend_df)

weekend_sleeper = df[
    (df["class_type"] == "sleeper") &
    (df["is_weekend"] == 1)
]
print(weekend_sleeper)


print(df["confirmed"].mean())


df["class_type_num"] = df["class_type"].map({
    "sleeper": 1,
    "AC": 0
})

print(df)

X = df[["class_type_num", "is_weekend"]]
y = df["confirmed"]

print(X)
print(y)



from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)

print("Model trained successfully")


test_data = [[1, 1]]  # sleeper=1, weekend=1

prediction = model.predict(test_data)
probability = model.predict_proba(test_data)

print("Prediction:", prediction)
print("Probability:", probability)


def predict_confirmation(class_type, is_weekend):
    class_num = 1 if class_type == "sleeper" else 0
    result = model.predict_proba([[class_num, is_weekend]])[0][1]
    return round(result * 100, 2)

chance = predict_confirmation("sleeper", 1)
print(f"Confirmation chance: {chance}%")
