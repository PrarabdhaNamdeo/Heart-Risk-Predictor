❤️ Heart Disease Risk Prediction System

A machine learning–powered web application that predicts a patient's heart disease risk level based on clinical input values. This project uses Random Forest Classifier, trained on the UCI Heart Disease dataset, and deployed using Streamlit Cloud.

✅ Features

🧠 Machine Learning Model (Random Forest Classifier)

🩺 Predicts Low, Mild, Moderate, High, Very High risk

🌐 Interactive Web App built using Streamlit

📊 Encodes and processes user inputs in real-time

📁 Uses saved model file (heart_model.pkl) for deployment

🚀 Fully hosted online via Streamlit Cloud

✅ Input Guide — What Each Term Means
1. Age
Your current age in years.

2. Sex
Biological sex:
Male    Female

3. Chest Pain Type (cp)
This describes the type of chest discomfort you feel:
Value	                            Meaning	                        Simple Explanation
0	                             Typical Angina	           Chest pain while doing activity/exercise
1	                             Atypical Angina	         Chest pain but not clearly heart-related
2	                             Non-Anginal Pain	         Chest pain not related to the heart
3	                             Asymptomatic	             No chest pain, but other symptoms may exist

4. Resting Blood Pressure (trestbps)
Your blood pressure when resting (in mm Hg).
Normal: around 120/80.
You enter only the systolic value (e.g., 130).

5. Cholesterol (chol)
Amount of cholesterol in your blood (mg/dl).
Less than 200 → Good
200–239 → Borderline
240+ → High

6. Fasting Blood Sugar (fbs)
Blood sugar level after fasting for at least 8 hours.
Value                     	Meaning
0	                       Below 120 mg/dl
1	                       Above 120 mg/dl (higher than normal)

7. Resting ECG (restecg)
Result of resting electrocardiogram.
Value	                      Meaning
0	                        Normal ECG
1	                        ST-T wave abnormality (possible heart issue)
2	                        Left ventricular hypertrophy (thick heart muscle)

8. Maximum Heart Rate (thalach)
Your highest heart rate achieved during exercise.
Normal range: 100–200 depending on age.

9. Exercise-Induced Angina (exang)
Chest pain caused by physical activity.
Value	                      Meaning
0	                            No
1	                            Yes
   
10. Oldpeak
Drop in ST segment on ECG after exercise.
Shows how much the heart is affected by exercise.
Example: 1.0, 2.5, 3.0, etc.
Higher values = higher risk.

11. Slope of ST Segment (slope)
Shape of the heart ECG during peak exercise.
Value	                                  Meaning
0	                                Upsloping (normal)
1	                                Flat (possible issue)
2	                                Downsloping (highest risk)
    
12. CA (Number of Vessels Colored)
Number of major blood vessels seen in an imaging test.
Values range from 0 to 3.
Higher value = more blockage detected.

13. Thal (Thalassemia Test Result)
Blood flow abnormality test.
Value	             Meaning
0	             Normal blood flow
1	             Fixed defect (older damage)
2	             Reversible defect (blood cannot reach properly)
3	             Severe defect
