import zipfile 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# from sklearn.preprocessing import MinMaxScaler

blood_pressure_and_cholesterol = pd.read_csv("data/2005-2006/Blood_Pressure_Cholesterol.csv")
diabetes = pd.read_csv("data/2005-2006/Diabetes.csv")
cholesterolldl_trigly_ApoB = pd.read_csv("data/2005-2006/Cholesterol - LDL_Triglyceride_Apoliprotein (ApoB).csv")
demographics = pd.read_csv("data/2005-2006/Demographics.csv")
hbA1c = pd.read_csv("data/2005-2006/Glycohemoglobin.csv", dtype = float)
physical_individual_act = pd.read_csv("data/2005-2006/Physical_Activity - Individual_Activities.csv")
physical_act = pd.read_csv("data/2005-2006/Physical_Activity.csv")
plasma_fasting_insulin = pd.read_csv("data/2005-2006/Plasma_Fasting_Glucose_Insulin.csv")
sleep_data = pd.read_csv("data/2005-2006/Sleep_Disorders.csv")


masterlist = blood_pressure_and_cholesterol.merge(diabetes,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(cholesterolldl_trigly_ApoB,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(demographics,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(hbA1c,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(physical_individual_act,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(physical_act,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(plasma_fasting_insulin,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(sleep_data,left_on = "SEQN",right_on = "SEQN")

## understanding features (columns) in the data
# Separate numerical and categorical columns
numerical_cols = masterlist.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = masterlist.select_dtypes(include=["object"]).columns

## handle missing values (remove rows)
masterlist.isnull().sum()
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


blood_pressure_and_cholesterol_columns_to_drop = [col for col in masterlist.columns if col not in 
                                                  ["BPQ020", "BPQ060", "BPQ080", "BPQ090A", "BPQ090C"]]
BPC_selected_features = masterlist.drop(columns=blood_pressure_and_cholesterol_columns_to_drop)


diabetes_columns_to_drop = [col for col in masterlist.columns if col not in 
                            ["DIQ010", "DID040", "DIQ220", "DIQ190A", "DIQ190B", "DIQ080", "DIQ230", "DID260", 
                             "DIQ280", "DIQ300S", "DIQ300D"]]
diabetes_selected_features = masterlist.drop(columns=diabetes_columns_to_drop)


physical_act_columns_to_drop = [col for col in masterlist.columns if col not in 
                                ["PAQ180", "PAD200", "PAD320", "PAD440", "PAD460", "PAQ500"]]
physical_act_selected_features = masterlist.drop(columns=physical_act_columns_to_drop)


physical_individual_act_columns_to_drop = [col for col in masterlist.columns if col not in 
                                ["PADACTIV", "PADLEVEL", "PADDURAT", "PADMETS"]]
physical_individual_act_selected_features = masterlist.drop(columns=physical_individual_act_columns_to_drop)


sleep_data_columns_to_drop = [col for col in masterlist.columns if col not in 
                                ["SLD010H", "SLQ060", "SLQ070A", "SLQ070B", "SLQ070C"
                                 "SLQ080", "SLQ090", "SLQ110", "SLQ130", "SLQ170", "SLQ180", "SLQ210"]]
sleep_selected_features = masterlist.drop(columns=sleep_data_columns_to_drop)


cholesterolldl_trigly_ApoB_columns_to_drop = [col for col in masterlist.columns if col not in 
                                ["LBXTR", "LBDTRSI", "LBDLDL", "LBDLDLSI", "LBXAPB", "LBDAPBSI"]]
cholesterolldl_trigly_ApoB_selected_features = masterlist.drop(columns=cholesterolldl_trigly_ApoB_columns_to_drop)


plasma_fasting_insulin_columns_to_drop = [col for col in masterlist.columns if col not in 
                                ["LBXGLU", "LBDGLUSI", "LBXIN", "LBDINSI", "PHAFSTHR", "PHAFSTMN"]]
plasma_fasting_insulin_selected_features = masterlist.drop(columns=plasma_fasting_insulin_columns_to_drop)


hbA1c_columns_to_drop = [col for col in masterlist.columns if col not in ["LBXGH"]]
hbA1c_selected_features = masterlist.drop(columns=hbA1c_columns_to_drop)


demographics_columns_to_drop = [col for col in masterlist.columns if col not in ["RIAGENDR", "RIDAGEMN", "RIDRETH1"]]
demographics_selected_features = masterlist.drop(columns=demographics_columns_to_drop)


## transform data - encoding categorical variables
    # masterlist = pd.get_dummies(masterlist) # , columns=['categorical_column']

## normalizing numerical data to keep values in similar range
    # scaler = MinMaxScaler()
    # masterlist[['numerical_column']] = scaler.fit_transform(masterlist[['numerical_column']])

## data visualization
# relationship between multiple numerical values

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

plt.show()



masterlist.to_csv('selected_features.csv', sep='\t', index=False)   



print(masterlist)



