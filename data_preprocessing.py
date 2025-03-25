# data_preprocessing.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore
from data_cleaning.diabetes import clean_diab_age_column, clean_diab_since_saw_specialist_column, clean_diab_last_A1C_level, clean_diab_when_diagnosis, clean_diab_how_often_check_blood_sugar, clean_diab_systolic_blood_pressure_val, clean_diab_diastolic_blood_pressure_val
from data_cleaning.sleep import clean_sleep_amount_of_sleep
from data_cleaning.physicalActivity import clean_physAct_avg_level, clean_physAct_indiv_avg_duration
from data_cleaning.demographics import clean_demographic_age
from data_cleaning.cholesterol import clean_cholesterol_ApoB
from data_cleaning.insulin import clean_plasma_fasting_glucose_insulin
from data_cleaning.glycohemoglobin import clean_glycohemoglobin

def prepare_data():

    # Load CSV files
    blood_pressure_and_cholesterol = pd.read_csv("raw_data/2005-2006/Blood_Pressure_Cholesterol.csv")
    diabetes = pd.read_csv("raw_data/2005-2006/Diabetes.csv")
    cholesterolldl_trigly_ApoB = pd.read_csv("raw_data/2005-2006/Cholesterol - LDL_Triglyceride_Apoliprotein (ApoB).csv")
    demographics = pd.read_csv("raw_data/2005-2006/Demographics.csv")
    hbA1c = pd.read_csv("raw_data/2005-2006/Glycohemoglobin.csv", dtype=float)
    physical_act_individual = pd.read_csv("raw_data/2005-2006/Physical_Activity - Individual_Activities.csv")
    physical_act = pd.read_csv("raw_data/2005-2006/Physical_Activity.csv")
    plasma_fasting_insulin = pd.read_csv("raw_data/2005-2006/Plasma_Fasting_Glucose_Insulin.csv")
    sleep_data = pd.read_csv("raw_data/2005-2006/Sleep_Disorders.csv")

    """ blood_pressure_and_cholesterol_20078 = pd.read_csv("raw_data/2007-2008/Blood_Pressure_Cholesterol.csv")
    diabetes_20078 = pd.read_csv("raw_data/2007-2008/Diabetes.csv")
    cholesterolldl_trigly_ApoB_20078 = pd.read_csv("raw_data/2007-2008/ApoB.csv")
    demographics_20078 = pd.read_csv("raw_data/2007-2008/Demographics.csv")
    hbA1c_20078 = pd.read_csv("raw_data/2007-2008/Glycohemoglobin.csv", dtype=float)
    #physical_act_individual_20078 = pd.read_csv("raw_data/2007-2008/Physical_Activity - Individual_Activities.csv")
    physical_act_20078 = pd.read_csv("raw_data/2007-2008/Physical_Activity.csv")
    plasma_fasting_insulin_20078 = pd.read_csv("raw_data/2007-2008/Plasma_Fasting_Glucose_Insulin.csv")
    sleep_data_20078 = pd.read_csv("raw_data/2007-2008/Sleep_Disorders.csv") """

    # Merge data on key 'SEQN'
    masterlist = (
        blood_pressure_and_cholesterol
        .merge(diabetes, on="SEQN")
        .merge(cholesterolldl_trigly_ApoB, on="SEQN")
        .merge(demographics, on="SEQN")
        .merge(hbA1c, on="SEQN")
        .merge(physical_act_individual, on="SEQN")
        .merge(physical_act, on="SEQN")
        .merge(plasma_fasting_insulin, on="SEQN")
        .merge(sleep_data, on="SEQN")
    )
    
    # Merge data on key 'SEQN'
    """ masterlist20078 = (
        blood_pressure_and_cholesterol_20078
        .merge(diabetes_20078, on="SEQN")
        .merge(cholesterolldl_trigly_ApoB_20078, on="SEQN")
        .merge(demographics_20078, on="SEQN")
        .merge(hbA1c_20078, on="SEQN")
        #.merge(physical_act_individual_20078, on="SEQN")
        .merge(physical_act_20078, on="SEQN")
        .merge(plasma_fasting_insulin_20078, on="SEQN")
        .merge(sleep_data_20078, on="SEQN")
    ) """
    """ print(masterlist.shape[0])
    masterlist = pd.concat([masterlist,masterlist20078], ignore_index=True)
    print(masterlist.shape[0]) """

    # Remove duplicates
    masterlist.drop_duplicates(inplace=True)

    # Optional sampling (90%)
    #masterlist = masterlist.sample(frac=0.9, random_state=42)

    # Select relevant features
    selected_features = {
        "BPC": ["BPQ020"],

        "Diabetes": ["DIQ010", "DID040", "DIQ220", "DIQ190A", "DIQ190B", "DIQ230", "DID260", "DIQ280", "DIQ300S", "DIQ300D"],
        
        "Physical_Activity": ["PAQ180"],
        "Physical_act_individual": ["PADACTIV", "PADDURAT"],
        "Sleep": ["SLD010H"],


        "Cholesterol_LDL_Trigly_ApoB": ["LBXAPB"],
        "Plasma_Fasting_Insulin": ["LBDINSI"],
        "HbA1c": ["LBXGH"],

        "Demographics": ["RIAGENDR", "RIDAGEMN"]
    }

    # Create a dictionary of DataFrames for each feature group
    feature_dataframes = {name: masterlist[["SEQN"] + cols] for name, cols in selected_features.items()}

    # Concatenate them
    combined_selected_features = pd.concat(feature_dataframes.values(), axis=1)

    # Remove duplicate SEQN columns
    combined_selected_features = combined_selected_features.loc[:, ~combined_selected_features.columns.duplicated()]

    # Sort by SEQN
    combined_selected_features.sort_values(by="SEQN", inplace=True)

    # Replace special codes with numeric values or NaN

    ## diabetes
    """ combined_selected_features['DID040'] = clean_diab_age_column(combined_selected_features['DID040'])
    combined_selected_features['DIQ230'] = clean_diab_since_saw_specialist_column(combined_selected_features['DIQ230'])
    combined_selected_features['DIQ280'] = clean_diab_last_A1C_level(combined_selected_features['DIQ280'])
    combined_selected_features['DIQ220'] = clean_diab_when_diagnosis(combined_selected_features['DIQ220'])
    combined_selected_features['DID260'] = clean_diab_how_often_check_blood_sugar(combined_selected_features['DID260'])
    combined_selected_features['DIQ300S'] = clean_diab_systolic_blood_pressure_val(combined_selected_features['DIQ300S'])
    combined_selected_features['DIQ300D'] = clean_diab_diastolic_blood_pressure_val(combined_selected_features['DIQ300D'])

    ## sleep
    combined_selected_features['SLD010H'] = clean_sleep_amount_of_sleep(combined_selected_features['SLD010H'])

    ## physical activity 
    combined_selected_features['PAQ180'] = clean_physAct_avg_level(combined_selected_features['PAQ180'])
    combined_selected_features['PADDURAT'] = clean_physAct_indiv_avg_duration(combined_selected_features['PADDURAT'])

    ## demographics
    combined_selected_features['RIDAGEMN'] = clean_demographic_age(combined_selected_features['RIDAGEMN'])

    ## cholesterol/apob levels
    combined_selected_features['LBXAPB'] = clean_cholesterol_ApoB(combined_selected_features['LBXAPB'])

    ## glycohemoglobin
    combined_selected_features['LBXGH'] = clean_glycohemoglobin(combined_selected_features['LBXGH'])

    ## insulin
    combined_selected_features['LBDINSI'] = clean_plasma_fasting_glucose_insulin(combined_selected_features['LBDINSI'])
 """
    # Calculate the mean of each column
    #column_means = combined_selected_features.mean().round(2)
    
    # Fill NaN values with the mean of the respective column
    #cleaned_combined_selected_features = combined_selected_features.fillna(column_means)

    return combined_selected_features


def save_cleaned_data(df, data_path="selected_features.csv", stats_path="selected_features_stats.csv"):
    if not df.empty:
        df.to_csv(data_path, sep='\t', index=False)
        # Save summary statistics
        stats_df = df.describe()
        stats_df.to_csv(stats_path, sep='\t', index=True)
    else:
        print("No data to save.")
