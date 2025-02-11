import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load pre-trained models and scalers
suitability_model = joblib.load("suitability_model.pkl")
suitability_scaler = joblib.load("suitability_scaler.pkl")

tensile_strength_model = joblib.load("tensile_strength_model.pkl")
tensile_strength_scaler = joblib.load("tensile_strength_scaler.pkl")

shear_modulus_model = joblib.load("shear_modulus_model.pkl")
shear_modulus_scaler = joblib.load("shear_modulus_scaler.pkl")

density_model = joblib.load("density_model.pkl")
density_scaler = joblib.load("density_scaler.pkl")

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
    
    Use the sidebar to navigate between tasks and provide the required inputs for predictions.
    """
)

# Sidebar navigation
st.sidebar.title("Navigation")
task = st.sidebar.radio(
    "Choose a task:",
    ("Material Suitability", "Ultimate Tensile Strength Prediction", "Shear Modulus Prediction", "Density Prediction"),
)

# Helper function for standardizing inputs
def standardize_input(input_data, scaler):
    return scaler.transform(np.array(input_data).reshape(1, -1))

### Task 1: Material Suitability ###
if task == "Material Suitability":
    st.header("Material Suitability Prediction")
    
    # Input fields for suitability prediction
    st.markdown("Provide the following material properties:")
    su = st.number_input("Ultimate Tensile Strength (Su) [MPa]", min_value=0.0)
    sy = st.number_input("Yield Strength (Sy) [MPa]", min_value=0.0)
    e = st.number_input("Elastic Modulus (E) [MPa]", min_value=0.0)
    g = st.number_input("Shear Modulus (G) [MPa]", min_value=0.0)
    mu = st.number_input("Poisson's Ratio (mu)", min_value=0.0, max_value=1.0)
    ro = st.number_input("Density (Ro) [kg/m³]", min_value=0.0)

    # Predict button
    if st.button("Check Suitability"):
        try:
            # Prepare input data and predict suitability
            input_data = [su, sy, e, g, mu, ro]
            standardized_data = standardize_input(input_data, suitability_scaler)
            prediction = suitability_model.predict(standardized_data)
            result = "Suitable" if prediction[0] == 1 else "Not Suitable"
            st.success(f"Material Suitability: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

### Task 2: Ultimate Tensile Strength Prediction ###
elif task == "Ultimate Tensile Strength Prediction":
    st.header("Ultimate Tensile Strength Prediction")
    
    # Input fields for tensile strength prediction
    st.markdown("Provide the following material properties:")
    sy = st.number_input("Yield Strength (Sy) [MPa]", min_value=0.0)
    e = st.number_input("Elastic Modulus (E) [MPa]", min_value=0.0)
    g = st.number_input("Shear Modulus (G) [MPa]", min_value=0.0)
    mu = st.number_input("Poisson's Ratio (mu)", min_value=0.0, max_value=1.0)
    ro = st.number_input("Density (Ro) [kg/m³]", min_value=0.0)

    # Predict button
    if st.button("Predict Ultimate Tensile Strength"):
        try:
            # Prepare input data and predict tensile strength
            input_data = [sy, e, g, mu, ro]
            standardized_data = standardize_input(input_data, tensile_strength_scaler)
            prediction = tensile_strength_model.predict(standardized_data)
            st.success(f"Predicted Ultimate Tensile Strength: {prediction[0]:.2f} MPa")
        except Exception as e:
            st.error(f"Error: {e}")

### Task 3: Shear Modulus Prediction ###
elif task == "Shear Modulus Prediction":
    st.header("Shear Modulus Prediction")
    
    # Input fields for shear modulus prediction
    st.markdown("Provide the following material properties:")
    su = st.number_input("Ultimate Tensile Strength (Su) [MPa]", min_value=0.0)
    sy = st.number_input("Yield Strength (Sy) [MPa]", min_value=0.0)
    e = st.number_input("Elastic Modulus (E) [MPa]", min_value=0.0)
    mu = st.number_input("Poisson's Ratio (mu)", min_value=0.0, max_value=1.0)
    ro = st.number_input("Density (Ro) [kg/m³]", min_value=0.0)

    # Predict button
    if st.button("Predict Shear Modulus"):
        try:
            # Prepare input data and predict shear modulus
            input_data = [su, sy, e, mu, ro]
            standardized_data = standardize_input(input_data, shear_modulus_scaler)
            prediction = shear_modulus_model.predict(standardized_data)
            st.success(f"Predicted Shear Modulus: {prediction[0]:.2f} MPa")
        except Exception as e:
            st.error(f"Error: {e}")

### Task 4: Density Prediction ###
elif task == "Density Prediction":
    st.header("Density Prediction")
    
    # Input fields for density prediction
    st.markdown("Provide the following material properties:")
    su = st.number_input("Ultimate Tensile Strength (Su) [MPa]", min_value=0.0)
    sy = st.number_input("Yield Strength (Sy) [MPa]", min_value=0.0)
    e = st.number_input("Elastic Modulus (E) [MPa]", min_value=0.0)
    g = st.number_input("Shear Modulus (G) [MPa]", min_value=0.0)
    mu = st.number_input("Poisson's Ratio (mu)", min_value=0.0, max_value=1.0)

    # Predict button
    if st.button("Predict Density"):
        try:
            # Prepare input data and predict density
            input_data = [su, sy, e, g, mu]
            standardized_data = standardize_input(input_data, density_scaler)
            prediction = density_model.predict(standardized_data)
            st.success(f"Predicted Density: {prediction[0]:.2f} kg/m³")
        except Exception as e:
            st.error(f"Error: {e}")
