# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

The Credit Card Approval Prediction project is a Machine Learning web application that predicts whether a credit card application will be approved or rejected based on customer information. The model is trained using historical customer data and uses a **Random Forest Classifier** to make accurate predictions.

The application helps banks and financial institutions automate the credit card approval process, reduce manual work, and make consistent lending decisions.

---

# 🚀 Features

- Predicts Credit Card Approval (Approved / Rejected)
- Machine Learning model using Random Forest Classifier
- User-friendly web interface
- Fast and accurate predictions
- Input validation
- Responsive design
- Easy deployment

---

# 🛠️ Technologies Used

## Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

# 📂 Project Structure

```
CreditCardApprovalPrediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── dataset/
│   └── credit_card_data.csv
│
└── model_training.py
```

---

# 📊 Dataset Features

The model is trained using approximately **30 customer features**, including:

1. Age
2. Gender
3. Annual Income
4. Employment Status
5. Years Employed
6. Education
7. Marital Status
8. Number of Dependents
9. Home Ownership
10. Residential Status
11. Credit Score
12. Existing Loans
13. Loan Amount
14. Loan Purpose
15. Monthly EMI
16. Debt-to-Income Ratio
17. Bank Balance
18. Savings Account
19. Current Account
20. Number of Credit Cards
21. Credit Utilization
22. Previous Defaults
23. Payment History
24. Number of Bank Accounts
25. Region
26. Occupation
27. Mobile Verified
28. Email Verified
29. PAN Verified
30. Aadhaar Verified

---

# ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Encode Categorical Features
5. Feature Scaling
6. Train-Test Split
7. Train Random Forest Classifier
8. Evaluate Model
9. Save Model
10. Deploy Flask Application

---

# 📈 Model Used

**Random Forest Classifier**

Advantages:

- High Accuracy
- Reduces Overfitting
- Handles Missing Values
- Works Well on Large Datasets
- Robust Performance

---

# 📊 Performance Metrics

Example Results:

| Metric | Score |
|---------|-------|
| Accuracy | 96% |
| Precision | 95% |
| Recall | 94% |
| F1 Score | 94% |

> **Note:** Metrics may vary depending on the dataset used.

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/CreditCardApprovalPrediction.git
```

Move into project folder

```bash
cd CreditCardApprovalPrediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

# 📦 Requirements

```text
Flask
numpy
pandas
scikit-learn
matplotlib
seaborn
joblib
```

Install using

```bash
pip install -r requirements.txt
```

---

# 🖥️ Application Workflow

1. Open the application.
2. Enter applicant details.
3. Click the **Predict** button.
4. The model analyzes the input.
5. The system displays either:
   - ✅ Approved
   - ❌ Rejected

---


---

# 🎯 Future Enhancements

- Deep Learning Model
- Explainable AI (SHAP/LIME)
- PDF Report Generation
- User Authentication
- Cloud Deployment
- Real-Time Credit Score API Integration
- Database Support
- Dashboard with Analytics

---

# 🎓 Learning Outcomes

- Data Preprocessing
- Feature Engineering
- Machine Learning Classification
- Random Forest Algorithm
- Model Evaluation
- Flask Web Development
- Model Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Create a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Rithesh Rock**

GitHub: https://github.com/yourusername

Email: youremail@example.com

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## Sample Prediction

| Feature | Value |
|----------|-------|
| Age | 30 |
| Annual Income | ₹600,000 |
| Credit Score | 760 |
| Employment | Salaried |
| Existing Loans | No |
| Previous Defaults | No |

### Prediction

```
Credit Card Status: APPROVED ✅
```

---

## Output

```
Applicant Details Received...

Loading Model...

Predicting...

Result:

✔ Credit Card Approved

Confidence: 96.5%
```

---
**Thank you for exploring the Credit Card Approval Prediction project!**
