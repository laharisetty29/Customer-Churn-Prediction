import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Dashboard")
st.write("Change customer values and predict churn probability.")

@st.cache_data
def load_data():
    df = pd.read_csv("churn-bigml-80.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

data = df.copy()
label_encoders = {}

for col in data.columns:
    if data[col].dtype == "object" or data[col].dtype == "bool":
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col].astype(str))
        label_encoders[col] = le

for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors="coerce")

data = data.fillna(0)

X = data.drop("Churn", axis=1)
y = data["Churn"].astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

st.subheader("Model Accuracy")
st.success(f"Accuracy: {accuracy * 100:.2f}%")

st.sidebar.header("Enter Customer Details")

user_input = {}

for col in X.columns:
    original_col = df[col]

    if original_col.dtype == "object":
        user_input[col] = st.sidebar.selectbox(
            col,
            sorted(original_col.astype(str).unique())
        )

    elif original_col.dtype == "bool":
        user_input[col] = st.sidebar.selectbox(
            col,
            [True, False]
        )

    else:
        user_input[col] = st.sidebar.number_input(
            col,
            value=float(original_col.mean())
        )

input_df = pd.DataFrame([user_input])

for col, encoder in label_encoders.items():
    if col in input_df.columns:
        input_df[col] = encoder.transform(input_df[col].astype(str))

for col in input_df.columns:
    input_df[col] = pd.to_numeric(input_df[col], errors="coerce")

input_df = input_df.fillna(0)

st.subheader("Selected Customer Details")
st.dataframe(pd.DataFrame([user_input]))

if st.button("Predict Churn"):

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    not_churn_probability = probabilities[0] * 100
    churn_probability = probabilities[1] * 100

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Churn Probability", f"{churn_probability:.2f}%")
        st.progress(min(int(churn_probability), 100))

    with col2:
        st.metric("Not Churn Probability", f"{not_churn_probability:.2f}%")
        st.progress(min(int(not_churn_probability), 100))

    if prediction == 1:
        st.error("🚨 Final Prediction: Customer is likely to Churn")
        st.error("🔴 Risk Level: High")
    else:
        st.success("✅ Final Prediction: Customer is not likely to Churn")

        if churn_probability >= 40:
            st.warning("🟡 Risk Level: Medium")
        else:
            st.success("🟢 Risk Level: Low")