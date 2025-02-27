import zipfile 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

blood_pressure_and_cholesterol = pd.read_csv("data/2005-2006/Blood_Pressure_Cholesterol.csv")
diabetes = pd.read_csv("data/2005-2006/Diabetes.csv")
cholesterolldl_trigly_ApoB = pd.read_csv("data/2005-2006/Cholesterol - LDL_Triglyceride_Apoliprotein (ApoB).csv")
demographics = pd.read_csv("data/2005-2006/Demographics.csv")
hbA1c = pd.read_csv("data/2005-2006/Glycohemoglobin.csv", dtype = float)
physical_individual_act = pd.read_csv("data/2005-2006/Physical_Activity - Individual_Activities.csv")
physical_act = pd.read_csv("data/2005-2006/Physical_Activity.csv")
plasma_fasting_insulin = pd.read_csv("data/2005-2006/Plasma_Fasting_Glucose_Insulin.csv")
sleep_data = pd.read_csv("data/2005-2006/Sleep_Disorders.csv")


masterlist = (
    blood_pressure_and_cholesterol
    .merge(diabetes, on="SEQN")
    .merge(cholesterolldl_trigly_ApoB, on="SEQN")
    .merge(demographics, on="SEQN")
    .merge(hbA1c, on="SEQN")
    .merge(physical_individual_act, on="SEQN")
    .merge(physical_act, on="SEQN")
    .merge(plasma_fasting_insulin, on="SEQN")
    .merge(sleep_data, on="SEQN")
)

# Remove all rows with any missing values
masterlist.dropna(inplace=True)

""" 
## fill missing values with mean/median/mode
masterlist.fillna(masterlist.mean(), inplace=True)  # Numeric columns
masterlist.fillna(masterlist.mode().iloc[0], inplace=True)  # Categorical columns """

## handle outliers
Q1 = masterlist.quantile(0.25)
Q3 = masterlist.quantile(0.75)
IQR = Q3 - Q1
masterlist_outliers_removed = masterlist[~((masterlist < (Q1 - 1.5 * IQR)) | (masterlist > (Q3 + 1.5 * IQR))).any(axis=1)]

## remove duplicate records
masterlist.drop_duplicates(inplace=True)

## remove redundant rows
masterlist.sample(frac=0.5, random_state=42) #50% of data is kept

# Select relevant features for different categories**
selected_features = {
    "BPC": ["BPQ020"],
    "Diabetes": ["DIQ010", "DID040", "DIQ220", "DIQ190A", "DIQ190B", "DIQ080", "DIQ230", "DID260", "DIQ280", "DIQ300S", "DIQ300D"],
    "Physical_Activity": ["PAQ180"],
    "Physical_Individual_Activity": ["PADACTIV", "PADDURAT"],
    "Sleep": ["SLD010H"],
    "Cholesterol_LDL_Trigly_ApoB": ["LBXAPB"],
    "Plasma_Fasting_Insulin": ["LBDINSI"],
    "HbA1c": ["LBXGH"],
    "Demographics": ["RIAGENDR", "RIDAGEMN"]
}

# Drop columns that are not in the selected feature lists**
feature_dataframes = {name: masterlist[["SEQN"] + cols] for name, cols in selected_features.items()}

# Concatenate selected features into a single DataFrame**
combined_selected_features = pd.concat(feature_dataframes.values(), axis=1)

# Remove duplicate "SEQN" columns created due to concatenation**
combined_selected_features = combined_selected_features.loc[:, ~combined_selected_features.columns.duplicated()]

# Save cleaned and selected data to CSV**
combined_selected_features.to_csv('selected_features.csv', sep='\t', index=False)


""" 
plt.close("all")

# pair plot
sns.pairplot(BPC_selected_features) 
plt.title("Pair Plot of Selected Blood Pressure and Cholesterol Features")

sns.pairplot(diabetes_selected_features) 
plt.title("Pair Plot of Selected Diabetes Features")

sns.pairplot(physical_act_selected_features) 
plt.title("Pair Plot of Selected Physical Activity-Individual Activities Features")

sns.pairplot(sleep_selected_features) 
plt.title("Pair Plot of Selected Sleep Data Features")

sns.pairplot(cholesterolldl_trigly_ApoB_selected_features) 
plt.title("Pair Plot of Selected Cholesterol (HDL), Cholesterol (LDL), Triglycerides and ApoB Features")

sns.pairplot(plasma_fasting_insulin_selected_features) 
plt.title("Pair Plot of Selected Plasma Fasting Glucose and Insulin Features")

sns.pairplot(hbA1c_selected_features) 
plt.title("Pair Plot of Selected HBA1C Features")

sns.pairplot(demographics_selected_features) 
plt.title("Pair Plot of Selected Demographics Features")

# correlation heatmap
masterlist_selected = BPC_selected_features
corr_matrix = masterlist_selected.corr()
plt.figure(figsize=(8,6 ))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Selected Blood Pressure and Cholesterol Features")

plt.show() """




