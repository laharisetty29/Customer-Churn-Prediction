# Customer Churn Prediction

A Machine Learning and Streamlit web application that predicts whether a customer is likely to churn or not based on telecom customer data.

## Project Overview

Customer churn is one of the major challenges for telecom companies. This project uses Machine Learning to analyze customer usage patterns and predict churn probability. The application provides an interactive Streamlit dashboard where users can enter customer details and instantly receive churn predictions.

## Features

* Customer Churn Prediction using Machine Learning
* Interactive Streamlit Dashboard
* Churn Probability Score
* Customer Risk Level Classification
* Dataset Preview
* Churn Distribution Visualization
* Real-Time Customer Prediction
* User-Friendly Interface

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Random Forest Classifier

## Dataset

The project uses a telecom customer churn dataset:

**Dataset File:** `churn-bigml-80.csv`

**Target Variable:** `Churn`

## Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── churn-bigml-80.csv
├── requirements.txt
├── README.md
└── Customer_Churn_Prediction.ipynb
```

## Installation

### Clone the Repository

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

## Run the Application

```bash
python -m streamlit run app.py
```

After running the command, Streamlit will automatically open the application in your browser.

## How It Works

1. Load the customer churn dataset.
2. Preprocess categorical and numerical features.
3. Train a Random Forest Classifier.
4. Accept customer details through the Streamlit interface.
5. Predict churn probability.
6. Display prediction results and risk level.

## Sample Inputs

### Likely To Churn

```text
International Plan = Yes
Voice Mail Plan = No
Total Day Minutes = 320
Total Day Charge = 55
Customer Service Calls = 6
```

### Not Likely To Churn

```text
International Plan = No
Voice Mail Plan = Yes
Total Day Minutes = 120
Total Day Charge = 20
Customer Service Calls = 0
```

## Model Information

**Algorithm Used:** Random Forest Classifier

### Why Random Forest?

* Handles large datasets efficiently
* Reduces overfitting
* High prediction accuracy
* Works well with mixed data types

## Application Output

The application displays:

* Customer is Likely to Churn
* Customer is Not Likely to Churn
* Churn Probability (%)
* Retention Probability (%)
* Customer Risk Level (Low, Medium, High)

## Future Enhancements

* Feature Importance Visualization
* Multiple Model Comparison
* Customer Segmentation Dashboard
* Downloadable Prediction Reports
* Cloud Deployment
* Advanced Business Insights

## Streamlit Dashboard

The dashboard includes:

* Dataset Preview
* Churn Distribution Analysis
* Customer Input Form
* Real-Time Predictions
* Probability Scores
* Risk Assessment

## Author

**Lahari Gadamsetty**

B.Tech – Computer Science and Engineering (Data Science)

---

⭐ If you found this project useful, consider giving it a star on GitHub.
