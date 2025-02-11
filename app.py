import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load pre-trained models
suitability_model = joblib.load("suitability_model.pkl")
tensile_strength_model = joblib.load("tensile_strength_model.pkl")
shear_modulus_model = joblib.load("shear_modulus_model.pkl")
density_model = joblib.load("density_model.pkl")

# Set up Streamlit app
st.set_page_config(page_title="Material Property Prediction App", layout="wide")
st.title("Material Property Prediction App")

st.markdown(
    """
    Welcome to the **Material Property Prediction App**! This app allows you to:
    - Predict the suitability of a material for specific use cases.
    - Predict material properties such as:
      - Ultimate Tensile Strength
      - Shear Modulus
      - Density
    """
)

# Sidebar navigation
st.sidebar.title("Navigation")
task = st.sidebar.radio(
    "Choose a task:",
    ("Material Suitability", "Ultimate Tensile Strength Prediction", "Shear Modulus Prediction", "Density Prediction"),
)

### Task 1: Material Suitability ###
if task == "Material Suitability":
    st.header("Material Suitability Prediction")
    
    su = st.number_input("Ultimate Tensile Strength (MPa)", min_value=0.0)
    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", min_value=0.0)
    g = st.number_input("Shear Modulus (MPa)", min_value=0.0)
    mu = st.number_input("Poisson's Ratio", min_value=0.0, max_value=1.0)
    ro = st.number_input("Density (kg/m³)", min_value=0.0)
    
    if st.button("Check Suitability"):
        input_data = np.array([su, sy, e, g, mu, ro]).reshape(1, -1)
        prediction = suitability_model.predict(input_data)
        result = "Suitable" if prediction[0] == 1 else "Not Suitable"
        st.success(f"Material Suitability: {result}")

### Task 2: Ultimate Tensile Strength Prediction ###
elif task == "Ultimate Tensile Strength Prediction":
    st.header("Ultimate Tensile Strength Prediction")
    
    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", min_value=0.0)
    g = st.number_input("Shear Modulus (MPa)", min_value=0.0)
    mu = st.number_input("Poisson's Ratio", min_value=0.0, max_value=1.0)
    ro = st.number_input("Density (kg/m³)", min_value=0.0)
    
    if st.button("Predict Ultimate Tensile Strength"):
        input_data = np.array([sy, e, g, mu, ro]).reshape(1, -1)
        prediction = tensile_strength_model.predict(input_data)
        st.success(f"Predicted Ultimate Tensile Strength: {prediction[0]:.2f} MPa")

### Task 3: Shear Modulus Prediction ###
elif task == "Shear Modulus Prediction":
    st.header("Shear Modulus Prediction")
    
    su = st.number_input("Ultimate Tensile Strength (MPa)", min_value=0.0)
    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", min_value=0.0)
    mu = st.number_input("Poisson's Ratio", min_value=0.0, max_value=1.0)
    ro = st.number_input("Density (kg/m³)", min_value=0.0)
    
    if st.button("Predict Shear Modulus"):
        input_data = np.array([su, sy, e, mu, ro]).reshape(1, -1)
        prediction = shear_modulus_model.predict(input_data)
        st.success(f"Predicted Shear Modulus: {prediction[0]:.2f} MPa")

### Task 4: Density Prediction ###
elif task == "Density Prediction":
    st.header("Density Prediction")
    
    su = st.number_input("Ultimate Tensile Strength (MPa)", min_value=0.0)
    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", min_value=0.0)
    g = st.number_input("Shear Modulus (MPa)", min_value=0.0)
    mu = st.number_input("Poisson's Ratio", min_value=0.0, max_value=1.0)
    
    if st.button("Predict Density"):
        input_data = np.array([su, sy, e, g, mu]).reshape(1, -1)
        prediction = density_model.predict(input_data)
        st.success(f"Predicted Density: {prediction[0]:.2f} kg/m³")
