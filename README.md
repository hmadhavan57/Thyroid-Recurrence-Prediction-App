# Thyroid-Recurrence-Prediction-App

## About the Dataset

This dataset contains 13 clinicopathologic features aimed at predicting the recurrence of well-differentiated thyroid cancer. The data was collected over a duration of 15 years, with each patient followed for at least 10 years.

### Source

The dataset was procured from the thyroid disease datasets provided by the UCI Machine Learning Repository which I had downloaded from Kaggle.

### Content

The dataset includes the following attributes:

- **Age**: The age of the patient at the time of diagnosis or treatment.
- **Gender**: The gender of the patient (male or female).
- **Smoking**:  Whether the patient is a smoker or not.
- **Hx Smoking**:  Smoking history of the patient (e.g., whether they have ever smoked).
- **Hx Radiotherapy**:  History of radiotherapy treatment for any condition.
- **Thyroid Function**:  The status of thyroid function, possibly indicating any abnormalities.
- **Physical Examination**:  Findings from a physical examination of the patient, which may include palpation of the thyroid gland and surrounding structures.
- **Adenopathy**:  Presence or absence of enlarged lymph nodes (adenopathy) in the neck region.
- **Pathology**:  Specific types of thyroid cancer as determined by pathology examination of biopsy samples.
- **Adenopathy**:  Presence or absence of enlarged lymph nodes (adenopathy) in the neck region.
- **Focality**:  Whether the cancer is unifocal (limited to one location) or multifocal (present in multiple locations).
- **Risk**:  The risk category of the cancer based on factors such as tumor size, extent of spread, and histological type.
- **T**:  Tumor classification based on size and extent of invasion into nearby structures.
- **N**:  Nodal classification indicating the involvement of lymph nodes.
- **M**:  Metastasis classification indicating the presence or absence of distant metastases.
- **Stage**: The overall stage of the cancer, typically determined by combining T, N, and M classifications.
- **Response**:  Response to treatment, indicating whether the cancer responded positively, negatively, or remained stable after treatment.
- **Recurred**:   Indicates whether the cancer has recurred after initial treatment.

## Model Development

Logistic Regression was utilized to predict the recurrence of well-differentiated thyroid cancer. The model was trained using the dataset that includes various clinicopathologic features.

### Training Process:

- **Features**: The model was trained using 13 features, including demographic and clinical information such as Age, Gender, Smoking History, Thyroid Function, and others.
- **Data Preprocessing**: Categorical variables were encoded using Label Encoding and One-Hot Encoding techniques.
- **Model**:  A Logistic Regression model was selected due to its suitability for binary classification tasks.

## Running the Streamlit App

To run your Streamlit app, follow these steps:

1. **Open a Terminal or Command Prompt**:
   - **Windows**: Use Command Prompt or PowerShell.
   - **macOS/Linux**: Use Terminal.

2. **Navigate to the Directory** where your `app.py` file is located. Use the `cd` command to change directories if needed.

## Running the Streamlit App

To run your Streamlit app, follow these steps:

1. **Open a Terminal or Command Prompt**:
   - **Windows**: Use Command Prompt or PowerShell.
   - **macOS/Linux**: Use Terminal.

2. **Navigate to the Directory** where your `app.py` file is located. Use the `cd` command to change directories if needed.

   ```bash
   cd path/to/your/directory

   
3. **Run the command**:

```bash
   Streamlit run app.py
 ```  
