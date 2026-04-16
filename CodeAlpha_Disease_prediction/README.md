#  Disease Prediction System

##  Overview
Machine learning is transforming healthcare by enabling early disease detection and accurate diagnosis. This project develops a predictive system that analyzes structured medical data such as age, symptoms, and clinical test results to estimate disease likelihood.

##  Methodology
The system uses datasets like Heart Disease, Diabetes, and Breast Cancer from the UCI Machine Learning Repository. Multiple classification algorithms are implemented, including:
- Support Vector Machine (SVM)
- Logistic Regression
- Random Forest
- XGBoost

The workflow includes data preprocessing, feature selection, model training, and performance evaluation.

##  Deployment
The best-performing model is deployed using Streamlit, allowing users to input medical data and receive real-time predictions through an interactive interface.

##  Tech Stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, Streamlit

##  Run the Project
pip install -r requirements.txt  
streamlit run app.py

##  Conclusion
This project demonstrates how machine learning can improve healthcare decision-making and support early diagnosis.
