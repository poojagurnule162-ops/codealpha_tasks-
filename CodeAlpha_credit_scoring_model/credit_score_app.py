# -*- coding: utf-8 -*-
"""
Credit Scoring Prediction App (Fixed Version)
"""

import pickle
import streamlit as st
import numpy as np

# Page config
st.set_page_config(page_title="Credit Score Prediction",
                   layout="centered",
                   page_icon="💳")

# Load model
model = pickle.load(open("C:/Users/pooja/OneDrive/Desktop/CodeAlpha_credit_scoring_model/credit_score_model.sav", "rb"))

# Title
st.title("💳 Credit Score Prediction System")

st.write("Enter the details below to predict loan approval status")

# ---------------- INPUT SECTION ---------------- #

income = st.number_input("Annual Income", min_value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)

term = st.selectbox(
    "Loan Term",
    ("Short Term", "Long Term")
)

credit_history = st.selectbox(
    "Credit History",
    ("Bad (0)", "Good (1)")
)

# ---------------- PROCESS INPUT ---------------- #

result = ""

if st.button("Predict Credit Status"):

    try:
        # Convert to log (IMPORTANT FIX)
        log_income = np.log(income) if income > 0 else 0
        log_loan_amount = np.log(loan_amount) if loan_amount > 0 else 0

        # Convert categorical values
        term_binary = 1 if term == "Long Term" else 0
        credit_history_binary = 1 if credit_history == "Good (1)" else 0

        # Final input
        user_input = [log_income, log_loan_amount, term_binary, credit_history_binary]

        # Prediction
        prediction = model.predict([user_input])

        if prediction[0] == 1:
            result = "✅ Loan Approved"
        else:
            result = "❌ Loan Not Approved"

    except Exception as e:
        result = "⚠️ Error in input. Please check values."

# Output
st.success(result)

# Info
st.info("Note: The system automatically converts values to log scale for accurate prediction.")