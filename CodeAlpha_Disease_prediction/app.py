# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:52:13 2026

@author: pooja
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:33:18 2026

@author: pooja
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/pooja/OneDrive/deployment/diabetes_model.sav', 'rb'))
 
heart_disease_model = pickle.load(open('C:/Users/pooja/OneDrive/deployment/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/pooja/OneDrive/deployment/parkinsons_model.sav', 'rb')) 

breast_cancer_model = pickle.load(open('C:/Users/pooja/OneDrive/deployment/breast_cancer_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu(
            'Multiple Disease Prediction System',
            ['Diabetes Prediction',
            'Heart Disease Prediction',
            'Breast Cancer Prediction'],
            menu_icon='hospital-fill',
            icons=['activity', 'heart', 'person', 'activity'],
            default_index=0
)
    


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


    
    # Breast Cancer Prediction Page
if selected == "Breast Cancer Prediction":

    st.title("Breast Cancer Prediction using ML")

    col1, col2, col3 = st.columns(3)

    # Mean values
    with col1:
        mean_radius = st.text_input('Mean Radius')
        mean_texture = st.text_input('Mean Texture')
        mean_perimeter = st.text_input('Mean Perimeter')
        mean_area = st.text_input('Mean Area')
        mean_smoothness = st.text_input('Mean Smoothness')

    with col2:
        mean_compactness = st.text_input('Mean Compactness')
        mean_concavity = st.text_input('Mean Concavity')
        mean_concave_points = st.text_input('Mean Concave Points')
        mean_symmetry = st.text_input('Mean Symmetry')
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')

    # Error values
    with col3:
        radius_error = st.text_input('Radius Error')
        texture_error = st.text_input('Texture Error')
        perimeter_error = st.text_input('Perimeter Error')
        area_error = st.text_input('Area Error')
        smoothness_error = st.text_input('Smoothness Error')

    col4, col5, col6 = st.columns(3)

    with col4:
        compactness_error = st.text_input('Compactness Error')
        concavity_error = st.text_input('Concavity Error')
        concave_points_error = st.text_input('Concave Points Error')
        symmetry_error = st.text_input('Symmetry Error')
        fractal_dimension_error = st.text_input('Fractal Dimension Error')

    # Worst values
    with col5:
        worst_radius = st.text_input('Worst Radius')
        worst_texture = st.text_input('Worst Texture')
        worst_perimeter = st.text_input('Worst Perimeter')
        worst_area = st.text_input('Worst Area')
        worst_smoothness = st.text_input('Worst Smoothness')

    with col6:
        worst_compactness = st.text_input('Worst Compactness')
        worst_concavity = st.text_input('Worst Concavity')
        worst_concave_points = st.text_input('Worst Concave Points')
        worst_symmetry = st.text_input('Worst Symmetry')
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    # Prediction
    cancer_diagnosis = ''

    if st.button("Breast Cancer Test Result"):

        user_input = [
            mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
            mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
            radius_error, texture_error, perimeter_error, area_error, smoothness_error,
            compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error,
            worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
            worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension
        ]

        user_input = [float(x) for x in user_input]

        prediction = breast_cancer_model.predict([user_input])

        if prediction[0] == 1:
            cancer_diagnosis = "The tumor is Malignant (Cancerous)"
        else:
            cancer_diagnosis = "The tumor is Benign (Non-Cancerous)"

    st.success(cancer_diagnosis)