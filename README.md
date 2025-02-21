# AlloyX - Material Property Prediction App

## Overview
AlloyX is a **machine learning-powered web application** designed to predict material properties such as **Ultimate Tensile Strength, Shear Modulus, Density**, and **Material Suitability** based on given input parameters. Built using **Streamlit**, AlloyX enables researchers and engineers to make data-driven decisions in material selection.

## Features
- **Material Suitability Prediction**: Determine if a material is suitable for specific applications.
- **Ultimate Tensile Strength Prediction**: Estimate the maximum stress a material can withstand.
- **Shear Modulus Prediction**: Calculate the material's rigidity.
- **Density Prediction**: Predict the mass per unit volume of the material.

## Dataset
The model is trained using a dataset containing various material properties, including:
- **Su** - Ultimate Tensile Strength (MPa)
- **Sy** - Yield Strength (MPa)
- **E** - Elastic Modulus (MPa)
- **G** - Shear Modulus (MPa)
- **mu** - Poisson's Ratio
- **Ro** - Density (kg/m³)
- **Use** - Whether the material is suitable for specific applications

### Sample Data Entry:
| Material | Su | Sy | E | G | mu | Ro | Use |
|----------|----|----|----|----|----|----|----|
| ANSI Steel SAE 1015 as-rolled | 421 | 314 | 207000 | 79000 | 0.3 | 7860 | TRUE |

## Technologies Used
- **Streamlit** - For building the interactive web application
- **Joblib** - For loading machine learning models
- **NumPy & Pandas** - For data processing and handling
- **Scikit-learn** - For training and implementing ML models

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Clone the Repository
```bash
git clone https://github.com/harshu0117/AlloyX.git
cd AlloyX
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
```bash
streamlit run app.py
```

## Model Usage
The app uses four pre-trained models:
- **suitability_model.pkl** - Predicts material suitability
- **tensile_strength_model.pkl** - Predicts Ultimate Tensile Strength
- **shear_modulus_model.pkl** - Predicts Shear Modulus
- **density_model.pkl** - Predicts Density

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Author
Developed by **Harsh Hanamanthagouda**

For any queries or feedback, reach out via GitHub Issues!

---

🚀 **Happy Predicting!**


