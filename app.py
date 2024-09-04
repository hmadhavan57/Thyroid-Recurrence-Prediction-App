import streamlit as st
import pandas as pd
import joblib

# Load the trained model and encoders
model = joblib.load('logistic_regression_model.pkl')
le_gender = joblib.load('le_gender.pkl')
le_smoking_history = joblib.load('le_smoking_history.pkl')
le_radiotherapy_history = joblib.load('le_radiotherapy_history.pkl')
le_focality = joblib.load('le_focality.pkl')
le_risk = joblib.load('le_risk.pkl')
le_tumor_classification = joblib.load('le_tumor_classification.pkl')
le_nodal_classification = joblib.load('le_nodal_classification.pkl')
le_metastasis_classification = joblib.load('le_metastasis_classification.pkl')
le_stage = joblib.load('le_stage.pkl')
encoder = joblib.load('one_hot_encoder.pkl')

# Define mappings for integer inputs
categorical_mapping = {
    'Gender': ['Select Gender', 'Male', 'Female'],
    'Smoking History': ['Select Smoking History', 'Yes', 'No'],
    'Radiotherapy History': ['Select Radiotherapy History', 'Yes', 'No'],
    'Focality': ['Select Focality', 'Unifocal', 'Multifocal'],
    'Risk': ['Select Risk', 'Low', 'Intermediate', 'High'],
    'Tumor Classification': ['Select Tumor Classification', 'T1', 'T2', 'T3', 'T4', 'T1a', 'T1b', 'T4a'],
    'Nodal classification': ['Select Nodal Classification', 'N0', 'N1', 'N2'],
    'Metastasis classification': ['Select Metastasis Classification', 'M0', 'M1'],
    'Stage': ['Select Stage', 'I', 'II', 'III', 'IV', 'V'],
    'Thyroid Function': ['Select Thyroid Function', 'Clinical Hypothyroidism', 'Euthyroid', 'Subclinical Hyperthyroidism', 'Subclinical Hypothyroidism'],
    'Physical Examination': ['Select Physical Examination', 'Multinodular goiter', 'Normal', 'Single nodular goiter-left', 'Single nodular goiter-right'],
    'Adenopathy': ['Select Adenopathy', 'Extensive', 'Left', 'No', 'Posterior', 'Right'],
    'Pathology': ['Select Pathology', 'Hurthel cell', 'Micropapillary', 'Papillary'],
    'Response': ['Select Response', 'Excellent', 'Indeterminate', 'Structural Incomplete']
}

st.set_page_config(page_title="Recurrence Prediction", layout="wide")
st.markdown("""
    <style>
    
    .title {
        color: #003366;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #002244;
    }
    .stSelectbox>div, .stNumberInput>div {
        background-color: #ffffff;
        border-radius: 5px;
        border: 1px solid #cccccc;
    }
    .stText {
        color: #003366;
    }
    .center {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Centered Title
st.markdown("<h1 class='title'> Thyroid Recurrence Prediction App</h1>", unsafe_allow_html=True)


# Input fields with empty choice as the default
age = st.number_input("Enter Age:", min_value=0, step=1, key='age')
gender_idx = st.selectbox("Select Gender:", range(len(categorical_mapping['Gender'])), format_func=lambda x: categorical_mapping['Gender'][x], key='gender')
smoking_history_idx = st.selectbox("Select Smoking History:", range(len(categorical_mapping['Smoking History'])), format_func=lambda x: categorical_mapping['Smoking History'][x], key='smoking_history')
radiotherapy_history_idx = st.selectbox("Select Radiotherapy History:", range(len(categorical_mapping['Radiotherapy History'])), format_func=lambda x: categorical_mapping['Radiotherapy History'][x], key='radiotherapy_history')
thyroid_function_idx = st.selectbox("Select Thyroid Function:", range(len(categorical_mapping['Thyroid Function'])), format_func=lambda x: categorical_mapping['Thyroid Function'][x], key='thyroid_function')
physical_examination_idx = st.selectbox("Select Physical Examination:", range(len(categorical_mapping['Physical Examination'])), format_func=lambda x: categorical_mapping['Physical Examination'][x], key='physical_examination')
adenopathy_idx = st.selectbox("Select Adenopathy:", range(len(categorical_mapping['Adenopathy'])), format_func=lambda x: categorical_mapping['Adenopathy'][x], key='adenopathy')
pathology_idx = st.selectbox("Select Pathology:", range(len(categorical_mapping['Pathology'])), format_func=lambda x: categorical_mapping['Pathology'][x], key='pathology')
focality_idx = st.selectbox("Select Focality:", range(len(categorical_mapping['Focality'])), format_func=lambda x: categorical_mapping['Focality'][x], key='focality')
risk_idx = st.selectbox("Select Risk:", range(len(categorical_mapping['Risk'])), format_func=lambda x: categorical_mapping['Risk'][x], key='risk')
tumor_classification_idx = st.selectbox("Select Tumor Classification:", range(len(categorical_mapping['Tumor Classification'])), format_func=lambda x: categorical_mapping['Tumor Classification'][x], key='tumor_classification')
nodal_classification_idx = st.selectbox("Select Nodal Classification:", range(len(categorical_mapping['Nodal classification'])), format_func=lambda x: categorical_mapping['Nodal classification'][x], key='nodal_classification')
metastasis_classification_idx = st.selectbox("Select Metastasis Classification:", range(len(categorical_mapping['Metastasis classification'])), format_func=lambda x: categorical_mapping['Metastasis classification'][x], key='metastasis_classification')
stage_idx = st.selectbox("Select Stage:", range(len(categorical_mapping['Stage'])), format_func=lambda x: categorical_mapping['Stage'][x], key='stage')
response_idx = st.selectbox("Select Response:", range(len(categorical_mapping['Response'])), format_func=lambda x: categorical_mapping['Response'][x], key='response')

if st.button("Predict"):
    if gender_idx == 0 or smoking_history_idx == 0 or radiotherapy_history_idx == 0 or thyroid_function_idx == 0 or physical_examination_idx == 0 or adenopathy_idx == 0 or pathology_idx == 0 or focality_idx == 0 or risk_idx == 0 or tumor_classification_idx == 0 or nodal_classification_idx == 0 or metastasis_classification_idx == 0 or stage_idx == 0 or response_idx == 0:
        st.error("Please fill in all the required fields.")
    else:
        # Encoding categorical variables
        gender_encoded = le_gender.transform([categorical_mapping['Gender'][gender_idx]])[0]
        smoking_history_encoded = le_smoking_history.transform([categorical_mapping['Smoking History'][smoking_history_idx]])[0]
        radiotherapy_history_encoded = le_radiotherapy_history.transform([categorical_mapping['Radiotherapy History'][radiotherapy_history_idx]])[0]
        focality_encoded = le_focality.transform([categorical_mapping['Focality'][focality_idx]])[0]
        risk_encoded = le_risk.transform([categorical_mapping['Risk'][risk_idx]])[0]
        tumor_classification_encoded = le_tumor_classification.transform([categorical_mapping['Tumor Classification'][tumor_classification_idx]])[0]
        nodal_classification_encoded = le_nodal_classification.transform([categorical_mapping['Nodal classification'][nodal_classification_idx]])[0]
        metastasis_classification_encoded = le_metastasis_classification.transform([categorical_mapping['Metastasis classification'][metastasis_classification_idx]])[0]
        stage_encoded = le_stage.transform([categorical_mapping['Stage'][stage_idx]])[0]

        # Create dictionary of inputs
        data = {
            'Age': age,
            'Gender': gender_encoded,
            'Smoking History': smoking_history_encoded,
            'Radiotherapy History': radiotherapy_history_encoded,
            'Focality': focality_encoded,
            'Risk': risk_encoded,
            'Tumor Classification': tumor_classification_encoded,
            'Nodal classification': nodal_classification_encoded,
            'Metastasis classification': metastasis_classification_encoded,
            'Stage': stage_encoded,
            f'Thyroid Function_{categorical_mapping["Thyroid Function"][thyroid_function_idx]}': 1,
            f'Physical Examination_{categorical_mapping["Physical Examination"][physical_examination_idx]}': 1,
            f'Adenopathy_{categorical_mapping["Adenopathy"][adenopathy_idx]}': 1,
            f'Pathology_{categorical_mapping["Pathology"][pathology_idx]}': 1,
            f'Response_{categorical_mapping["Response"][response_idx]}': 1
        }

        # Add missing features with value 0
        for col in model.feature_names_in_:
            if col not in data:
                data[col] = 0

        # Create DataFrame with the correct order of features
        input_df = pd.DataFrame(data, index=[0])[model.feature_names_in_]

        # Predict outcome
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        result = 'Recurred' if prediction[0] else 'Did Not Recur'
        st.markdown(f"<h2 style='color:#003366;text-align:center;'>Prediction: {result}</h2>", unsafe_allow_html=True)
        #st.markdown(f"<h3 style='color:#003366;'>Prediction Probability: {prediction_proba[0]}</h3>", unsafe_allow_html=True)
