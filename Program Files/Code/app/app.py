import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# ==========================================
# 1. GENERATE DUMMY CREDIT APPLICATION DATA
# ==========================================
# (Replacing a live dataset download with a structural simulation 
#  matching UCI or Kaggle credit card application formats)

np.random.seed(42)
n_samples = 1000

data = {
    'Gender': np.random.choice(['M', 'F'], n_samples),
    'Age': np.random.randint(18, 70, n_samples),
    'Annual_Income': np.random.randint(20000, 150000, n_samples),
    'Income_Type': np.random.choice(['Working', 'Commercial associate', 'State servant', 'Pensioner'], n_samples),
    'Education': np.random.choice(['Secondary', 'Higher education', 'Incomplete higher'], n_samples),
    'Family_Status': np.random.choice(['Married', 'Single', 'Civil marriage', 'Divorced'], n_samples),
    'Years_Employed': np.random.uniform(0, 40, n_samples),
    'Prior_Default': np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
    'Debt': np.random.uniform(0, 30000, n_samples),
    'Credit_Score': np.random.randint(300, 850, n_samples)
}

df = pd.DataFrame(data)

# Simulate an Approval logic (Target variable 'Approved': 1 = Yes, 0 = No)
# Real banks use complex rules; here we create a realistic synthetic relationship
score = (df['Annual_Income'] / 10000) + (df['Credit_Score'] / 50) + (df['Years_Employed'] * 2) - (df['Prior_Default'] * 20)
df['Approved'] = np.where(score > 25, 1, 0)

# ==========================================
# 2. FEATURE SELECTION & SEPARATION
# ==========================================
X = df.drop(columns=['Approved'])
y = df['Approved']

# Separate feature types for preprocessing
categorical_cols = ['Gender', 'Income_Type', 'Education', 'Family_Status']
numerical_cols = ['Age', 'Annual_Income', 'Years_Employed', 'Prior_Default', 'Debt', 'Credit_Score']

# ==========================================
# 3. DATA PREPROCESSING PIPELINE
# ==========================================
# Standardize numbers and One-Hot Encode categorical strings
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first'), categorical_cols)
    ])

# Split into Train and Test datasets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply processing
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# ==========================================
# 4. MODEL TRAINING (Random Forest)
# ==========================================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_processed, y_train)

# ==========================================
# 5. EVALUATION
# ==========================================
y_pred = model.predict(X_test_processed)

print("--- Model Performance ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==========================================
# 6. PREDICT ON A NEW APPLICATION
# ==========================================
new_application = pd.DataFrame([{
    'Gender': 'M',
    'Age': 35,
    'Annual_Income': 85000,
    'Income_Type': 'Commercial associate',
    'Education': 'Higher education',
    'Family_Status': 'Married',
    'Years_Employed': 7.5,
    'Prior_Default': 0,
    'Debt': 1200,
    'Credit_Score': 710
}])

processed_app = preprocessor.transform(new_application)
prediction = model.predict(processed_app)
probability = model.predict_proba(processed_app)[0][1]

print("\n--- New Application Prediction ---")
if prediction[0] == 1:
    print(f"Status: APPROVED 🎉 (Probability of Approval: {probability*100:.2f}%)")
else:
    print(f"Status: REJECTED ❌ (Probability of Approval: {probability*100:.2f}%)")