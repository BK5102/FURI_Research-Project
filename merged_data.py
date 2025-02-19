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

# merged_data = pd.merge(blood_pressure_and_cholesterol, diabetes, on="SEQN", how="inner")

masterlist = blood_pressure_and_cholesterol.merge(diabetes,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(cholesterolldl_trigly_ApoB,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(demographics,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(hbA1c,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(physical_individual_act,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(physical_act,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(plasma_fasting_insulin,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(sleep_data,left_on = "SEQN",right_on = "SEQN")


## checking structure 
    # print(masterlist.describe())
    # print(masterlist.isnull().sum())


## understanding features (columns) in the data
# Separate numerical and categorical columns
numerical_cols = masterlist.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = masterlist.select_dtypes(include=["object"]).columns

# print("Numerical Columns:", numerical_cols)
# print("Categorical Columns:", categorical_cols)


## handle missing values
masterlist.isnull().sum()

## remove rows with missing values
masterlist.dropna(inplace=True)

## fill missing values with mean/median/mode
masterlist.fillna(masterlist.mean(), inplace=True)  # Numeric columns
masterlist.fillna(masterlist.mode().iloc[0], inplace=True)  # Categorical columns

## handle outliers
Q1 = masterlist.quantile(0.25)
Q3 = masterlist.quantile(0.75)
IQR = Q3 - Q1
masterlist_outliers_removed = masterlist[~((masterlist < (Q1 - 1.5 * IQR)) | (masterlist > (Q3 + 1.5 * IQR))).any(axis=1)]

## remove duplicate records
masterlist.drop_duplicates(inplace=True)

## remove redundant rows
masterlist.sample(frac=0.5, random_state=42) #50% of data is kept



masterlist.to_csv('merged_and_cleaned_data.csv', sep='\t', index=True)   #change to True later 



print(masterlist)



