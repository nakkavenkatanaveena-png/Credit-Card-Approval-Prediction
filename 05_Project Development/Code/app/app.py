from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("label_encoders.pkl")

# Load dataset
data = pd.read_csv("credit_data.csv")

# Remove columns that are NOT input features
drop_cols = []

if "ID" in data.columns:
    drop_cols.append("ID")

if "TARGET" in data.columns:
    drop_cols.append("TARGET")

if "Class" in data.columns:
    drop_cols.append("Class")

data = data.drop(columns=drop_cols, errors="ignore")

feature_columns = list(data.columns)

print("Features:", feature_columns)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    values = {}

    for col in feature_columns:
        values[col] = request.form.get(col, 0)

    df = pd.DataFrame([values])

    # Encode categorical columns
    for col in df.columns:
        if col in encoders:
            try:
                df[col] = encoders[col].transform(df[col].astype(str))
            except:
                df[col] = 0
        else:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Ensure feature order matches training
    df = df.reindex(columns=feature_columns, fill_value=0)

    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)[0]

    if prediction == 0:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)