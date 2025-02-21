import streamlit as st
import numpy as np
import joblib

# Load pre-trained models
suitability_model = joblib.load("suitability_model.pkl")
tensile_strength_model = joblib.load("tensile_strength_model.pkl")
shear_modulus_model = joblib.load("shear_modulus_model.pkl")
density_model = joblib.load("density_model.pkl")

# Set up Streamlit app
st.set_page_config(page_title="AlloyX - Steel Alloy Property Predictor", layout="wide")
st.title("AlloyX - Steel Alloy Property Predictor")

st.markdown("""
## 🛠 User Guide:
- This app predicts properties of **steel alloys** based on input values.
- Ensure input values are **within the trained dataset range** for accurate predictions.
- Works best for steel alloys like **ANSI Steel SAE 1015, 1018, and 1020**.
- Entering values outside the typical range may lead to **unreliable predictions**.

### ✅ Supported Input Ranges:
- **Ultimate Tensile Strength (Su):** 386 MPa – 448 MPa
- **Yield Strength (Sy):** 284 MPa – 346 MPa
- **Elastic Modulus (E):** 207,000 MPa (constant)
- **Shear Modulus (G):** 79,000 MPa (constant)
- **Poisson’s Ratio (mu):** 0.3 (constant)
- **Density (Ro):** 7,860 kg/m³ (constant)
""")

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
    e = st.number_input("Elastic Modulus (MPa)", value=207000)
    g = st.number_input("Shear Modulus (MPa)", value=79000)
    mu = st.number_input("Poisson's Ratio", value=0.3)
    ro = st.number_input("Density (kg/m³)", value=7860)

    if st.button("Check Suitability"):
        input_data = np.array([su, sy, e, g, mu, ro]).reshape(1, -1)
        prediction = suitability_model.predict(input_data)
        result = "Suitable" if prediction[0] == 1 else "Not Suitable"
        st.success(f"Material Suitability: {result}")

### Task 2: Ultimate Tensile Strength Prediction ###
elif task == "Ultimate Tensile Strength Prediction":
    st.header("Ultimate Tensile Strength Prediction")

    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", value=207000)
    g = st.number_input("Shear Modulus (MPa)", value=79000)
    mu = st.number_input("Poisson's Ratio", value=0.3)
    ro = st.number_input("Density (kg/m³)", value=7860)

    if st.button("Predict Ultimate Tensile Strength"):
        input_data = np.array([sy, e, g, mu, ro]).reshape(1, -1)
        prediction = tensile_strength_model.predict(input_data)
        st.success(f"Predicted Ultimate Tensile Strength: {prediction[0]:.2f} MPa")

### Task 3: Shear Modulus Prediction ###
elif task == "Shear Modulus Prediction":
    st.header("Shear Modulus Prediction")

    su = st.number_input("Ultimate Tensile Strength (MPa)", min_value=0.0)
    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", value=207000)
    mu = st.number_input("Poisson's Ratio", value=0.3)
    ro = st.number_input("Density (kg/m³)", value=7860)

    if st.button("Predict Shear Modulus"):
        input_data = np.array([su, sy, e, mu, ro]).reshape(1, -1)
        prediction = shear_modulus_model.predict(input_data)
        st.success(f"Predicted Shear Modulus: {prediction[0]:.2f} MPa")

### Task 4: Density Prediction ###
elif task == "Density Prediction":
    st.header("Density Prediction")

    su = st.number_input("Ultimate Tensile Strength (MPa)", min_value=0.0)
    sy = st.number_input("Yield Strength (MPa)", min_value=0.0)
    e = st.number_input("Elastic Modulus (MPa)", value=207000)
    g = st.number_input("Shear Modulus (MPa)", value=79000)
    mu = st.number_input("Poisson's Ratio", value=0.3)

    if st.button("Predict Density"):
        input_data = np.array([su, sy, e, g, mu]).reshape(1, -1)
        prediction = density_model.predict(input_data)
        st.success(f"Predicted Density: {prediction[0]:.2f} kg/m³")
