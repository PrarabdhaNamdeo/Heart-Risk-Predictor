import streamlit as st
import pandas as pd
import pickle
import joblib

model = joblib.load("heart_model.pkl")

st.title("❤️ Heart Risk Prediction System")
st.write("Welcome! Enter Details and Symptoms to Predict Heart Disease Risk.")

age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["0", "1", "2", "3"])
trestbps = st.number_input("Resting Blood Pressure", 80, 200)
chol = st.number_input("Cholesterol", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar", ["0", "1"])
restecg = st.selectbox("Rest ECG", ["0", "1", "2"])
thalach = st.number_input("Maximum Heart Rate", 50, 220)
exang = st.selectbox("Exercise-Induced Angina", ["0", "1"])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0)
slope = st.selectbox("Slope", ["0", "1", "2"])
ca = st.number_input("Number of Major Vessels (0-3)", 0, 3)
thal = st.selectbox("Thal", ["0", "1", "2"])

if st.button("Predict"):
    data = [[age, 1 if sex=="Male" else 0, cp, trestbps, chol,
             fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

    pred = model.predict(data)[0]

    risk = {
        0: "✅ Very Low Risk",
        1: "🟡 Low Risk",
        2: "🟠 Moderate Risk",
        3: "🔴 High Risk",
        4: "🚨 Very High Risk"
    }

    st.success(f"Predicted Risk:  {risk[pred]}")
