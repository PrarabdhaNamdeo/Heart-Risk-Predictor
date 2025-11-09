# ❤️ Heart Disease Risk Prediction System

A machine learning–powered web application that predicts a patient's **heart disease risk level** based on clinical health parameters.  
This project uses a **Random Forest Classifier**, trained on the **UCI Heart Disease Dataset**, and deployed using **Streamlit Cloud**.

---

## ✅ Features

- 🧠 **Random Forest ML Model** trained on 5-class risk labels  
- 🩺 Predicts **Low, Mild, Moderate, High, Very High** heart risk levels  
- 🌐 **Interactive Web Interface** using Streamlit  
- 📊 Real-time preprocessing + prediction  
- 💾 Uses saved model file (`heart_model.pkl`)  
- 🚀 Fully deployed online through Streamlit Cloud  

---

## ✅ How It Works

1. User enters basic medical information  
2. Data is preprocessed using encoded values  
3. Trained ML model predicts risk category  
4. Risk label is mapped to a human-readable explanation  

---

# ✅ Input Guide — What Each Term Means

This section helps non-medical users understand what values they should enter.

---

## **Age**
Your current age (in years).

---

## **Sex**

| Value | Meaning |
|-------|---------|
| 0 | Female |
| 1 | Male |

---

## **Chest Pain Type (cp)**

| Value | Meaning | Simple Explanation |
|-------|---------|-------------------|
| 0 | Typical Angina | Chest pain during exercise/activity |
| 1 | Atypical Angina | Chest pain but not clearly heart-related |
| 2 | Non-Anginal Pain | Chest pain not related to the heart |
| 3 | Asymptomatic | No chest pain, but symptoms may exist |

---

## **Resting Blood Pressure (trestbps)**  
Systolic blood pressure at rest (e.g., 120, 130, 150).

- Normal: ~120  
- High: 140+  

---

## **Cholesterol (chol)** (mg/dl)

| Range | Meaning |
|--------|---------|
| < 200 | Desirable |
| 200–239 | Borderline High |
| ≥ 240 | High |

---

## **Fasting Blood Sugar (fbs)**

| Value | Meaning |
|-------|---------|
| 0 | Below 120 mg/dl |
| 1 | Above 120 mg/dl (higher than normal) |

---

## **Resting ECG Result (restecg)**

| Value | Meaning |
|-------|---------|
| 0 | Normal |
| 1 | ST-T wave abnormality (possible heart issue) |
| 2 | Left ventricular hypertrophy (thickening of heart muscle) |

---

## **Maximum Heart Rate (thalach)**  
Highest heart rate achieved during exercise.  
Typical range: 100–200 bpm.

---

## **Exercise-Induced Angina (exang)**

| Value | Meaning |
|-------|---------|
| 0 | No |
| 1 | Yes |

---

## **Oldpeak**  
ST depression induced by exercise relative to rest.  
Example: `1.0`, `2.6`, `3.0`.  
Higher = higher risk.

---

## **Slope of ST Segment (slope)**

| Value | Meaning |
|-------|---------|
| 0 | Upsloping (normal) |
| 1 | Flat (possible heart issue) |
| 2 | Downsloping (higher risk) |

---

## **CA — Number of Major Vessels Colored**

| Value | Meaning |
|-------|---------|
| 0 | No major blockage |
| 1 | One vessel affected |
| 2 | Two vessels affected |
| 3 | Three vessels affected |

Higher value = higher risk.

---

## **Thal (Thalassemia Test Result)**

| Value | Meaning |
|-------|---------|
| 0 | Normal blood flow |
| 1 | Fixed defect (old heart damage) |
| 2 | Reversible defect (blood cannot reach properly) |
| 3 | Severe defect (high risk) |

---

# ✅ Output — Risk Levels

| Predicted Number | Risk Level |
|------------------|------------|
| 0 | **Low Risk** |
| 1 | **Mild Risk** |
| 2 | **Moderate Risk** |
| 3 | **High Risk** |
| 4 | **Very High Risk** |

---

# ✅ Installation (Local Usage)

```bash
pip install -r requirements.txt
streamlit run app.py
