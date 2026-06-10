# 📊 Customer Churn Prediction

A Machine Learning and Streamlit-based web application that predicts whether a telecom customer is likely to churn or not using customer usage and service-related features.

---

## 🚀 Live Demo

🔗 **Streamlit App:**
https://customer-churn-prediction-eg5qlpbnbbosyh7rt3ptef.streamlit.app/

🔗 **GitHub Repository:**
https://github.com/laharisetty29/Customer-Churn-Prediction

---

## 📌 Project Overview

Customer churn prediction is an important business problem in the telecom industry. Retaining existing customers is often more cost-effective than acquiring new ones.

This project uses a **Random Forest Machine Learning Model** to analyze customer behavior and predict the likelihood of churn. The application is deployed using **Streamlit Cloud** for real-time predictions.

---

## ✨ Features

* Customer Churn Prediction
* Interactive Streamlit Dashboard
* Real-Time Customer Risk Assessment
* Churn Probability Score
* Not Churn Probability Score
* Risk Level Classification
* Customer Input Form
* Machine Learning-Based Predictions
* Cloud Deployment Using Streamlit

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Random Forest Classifier
* Git & GitHub

---

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── churn-bigml-80.csv
├── requirements.txt
├── README.md
└── Customer_Churn_Prediction.ipynb
```

---

## 📊 Dataset

Dataset used:

```text
churn-bigml-80.csv
```

Target Variable:

```text
Churn
```

The dataset contains customer demographics, usage patterns, service information, and churn status.

---

## 🤖 Machine Learning Model

### Algorithm Used

```text
Random Forest Classifier
```

### Why Random Forest?

* Handles complex datasets efficiently
* Reduces overfitting
* Provides high prediction accuracy
* Works with both numerical and categorical features

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/laharisetty29/Customer-Churn-Prediction.git
```

### Navigate to Project Folder

```bash
cd Customer-Churn-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## 📈 Application Workflow

1. Load telecom customer dataset
2. Preprocess customer data
3. Encode categorical variables
4. Train Random Forest model
5. Accept customer details through dashboard
6. Predict churn probability
7. Display prediction and risk level

---

## 🎯 Sample Test Cases

### High Churn Risk

```text
State = AK
Account length = 5
International plan = Yes
Voice mail plan = No
Customer service calls = 10
Total day minutes = 400
Total intl minutes = 25
```

Expected Output:

```text
Customer is likely to Churn
Risk Level: High
```

---

### Low Churn Risk

```text
State = CA
Account length = 150
International plan = No
Voice mail plan = Yes
Customer service calls = 0
Total day minutes = 100
Total intl minutes = 3
```

Expected Output:

```text
Customer is not likely to Churn
Risk Level: Low
```

---

## 📷 Dashboard Features

* Model Accuracy Display
* Customer Input Form
* Churn Probability
* Not Churn Probability
* Risk Classification
* Interactive Prediction Results

---

## 🚀 Future Enhancements

* Feature Importance Visualization
* Multiple Model Comparison
* Customer Segmentation
* Downloadable Prediction Reports
* Advanced Analytics Dashboard
* Explainable AI (XAI)

---

## 👩‍💻 Author

### Gadamsetty Lahari

🎓 B.Tech – Computer Science and Engineering (Data Science)

🔗 GitHub:
https://github.com/laharisetty29

🔗 LinkedIn:
https://www.linkedin.com/in/laharigadamsetty

---

⭐ If you found this project useful, please consider giving it a Star on GitHub.
