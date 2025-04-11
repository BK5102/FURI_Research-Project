# Supervised Learning for Early Detection of Chronic Diseases Using Wearable and Other Health Data in NHANES
## Spring '25

## This approach leverages wearable and other health data from the National Health and Nutrition Examination Survey (NHANES) to develop a Supervised Learning (SL) framework that detects pre-diabetes mellitus symptoms using factors such as hypertension, sleep and physical activity measurements from wearables.

## Overview
### More than 8 in 10 adults with prediabetes don't know they have it. 
### Large volumes of electronic health records hold promise in identifying trends in physical activity, sleep and hypertension linked to pre-diabetes. 
### This research project focuses on using real-time data from wearable devices and electronic health records (EHRs) available from the National Health and Nutrition Examination Survey (NHANES) to identify patterns that healthcare professionals and clinicians can use to detect common diseases before they become widespread. 
### Through this methodology, individuals do not have to consult a healthcare professional and instead use data from their wearables such as sleep patterns, physical activity, hypertension, etc to see if they have any symptoms of pre-diabetes mellitus.

## Motivation and Background
### As smartwatches become more and more popular, healthcare providers are often overwhelmed with large amounts of data. Sifting through this data takes time to identify meaningful patterns that may help indicate early signs of chronic conditions, such as heart disease or diabetes. The clear understanding of this data as a result of machine learning software can help make a positive impact in public health and the healthcare system, ultimately improving patient outcomes.
### Traditional methods rely on biochemical tests. While these can be accurate, they require blood draws, lab access, and can be costly or inaccessible in many low-resource settings. Also, they may not be suitable for continuous or large-scale community-level screening. 
### Early detection of pre-diabetes is vital for preventing the progression to type 2 diabetes. Identifying individuals at risk during the pre-diabetic stage allows for timely lifestyle and behavioral interventions, which can significantly reduce or delay the onset of full-blown diabetes. 
### The approach of this research project relies on self-reported data and wearable technology. Thus, promoting a scalable, low-cost, and early-stage screening.
### The American Diabetes Association (ADA) has a guideline for pre-diabetes. Modeling from this, the guideline chosen for this project uses three important variables: plasma fasting insulin levels, apolipoprotein b, and glycohemoglobin (hb1ac) levels from the NHANES dataset. 

## Methodology
### Dataset: 
  #### National Health and Nutrition Examination Survey (NHANES) 2005-2006 dataset
  #### Questionnare, Laboratory, Demographics Data
### Machine Learning Approach:
  #### Supervised Learning Framework using four performance models: Logistic Regression (66%), Support Vector Machine (69%), Random Forest (88%), XgBoost (89%).
  #### LASSO regularization (L1 and L2) to achieve lower variance and prevent overfitting. 
  #### Hyperparameter tuning such as t-test and chi-square test were used to compare p-values, however these methods failed to provide solid results.
### Evaluation Metric:
  #### Accuracy, F1 score among others such as precision and recall were used to compare and evaluate model performance. 
### Model Performance:
  #### Among the models, XgBoost performed the best with an accuracy of 89%. Additionally, regularization achieved lower variance and important features such as age and hypertension were identified using the SHAP values visualization method. 

## Repository Structure


## Installation and Setup
### Steps to clone repository:
`git clone https://github.com/BK5102/FURI_Research-Project.git`
`cd FURI_Research-Project`

### Setting up a virtual environment: 
# Create virtual environment (use 'venv' or any name you prefer)
`python -m venv venv`

#### Activate the virtual environment
##### On Windows:
`venv\Scripts\activate`
##### On macOS/Linux:
`source venv/bin/activate`

### Installing dependencies:
`pip install -r requirements.txt`

### Run code cells in Jupyter Notebook file 
final_analysis.ipynb


## Usage 
### Data Preprocessing Flowchart Link:
https://drive.google.com/file/d/1pIZAUt5SDjsy82e8fnXWyhTHmg3TjJfP/view?usp=sharing

## Results and Findings (Progress)
### Insights from feature importance analysis
  #### SHAP Value scores identified age and hypertension as the most important features 
  #### These risk factors can be monitored from wearable devices 
  #### Provides insights into important demographics such as gender (male/female)

## Future Work/Improvements
### Improving dataset size and diversity
### Building application
### Exploring additional non-biochemical features
### Deploying the model for real-world testing

## Contributors 
### Kabsoo Jang, PhD student under Professor Bing Si at Fulton Schools of Engineering, Arizona State University, Tempe, AZ

## References
### https://shorturl.at/X8kLQ
### https://shorturl.at/JPGKf 
