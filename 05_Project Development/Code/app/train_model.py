import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("credit_data.csv")

print("Columns in dataset:")
print(df.columns.tolist())

# Drop ID column if present
if "ID" in df.columns:
    df = df.drop(columns=["ID"])

# Possible target column names
possible_targets = [
    "TARGET",
    "target",
    "STATUS",
    "status",
    "Approved",
    "approved",
    "Label",
    "label",
    "Class",
    "class"
]

target_col = None

for col in possible_targets:
    if col in df.columns:
        target_col = col
        break

if target_col is None:
    print("\nERROR: No target column found.")
    print("Available columns are:")
    print(df.columns.tolist())
    exit()

print(f"\nUsing target column: {target_col}")

X = df.drop(columns=[target_col])
y = df[target_col]

# Encode categorical columns
encoders = {}

for col in X.columns:
    if X[col].dtype == "object":
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        encoders[col] = le

# Encode target if needed
if y.dtype == "object":
    le_target = LabelEncoder()
    y = le_target.fit_transform(y)

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Save files
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoders, "label_encoders.pkl")

print("\nModel saved successfully.")