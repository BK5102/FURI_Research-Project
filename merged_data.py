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

#merged_data = pd.merge(blood_pressure_and_cholesterol, diabetes, on="SEQN", how="inner")

masterlist = blood_pressure_and_cholesterol.merge(diabetes,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(cholesterolldl_trigly_ApoB,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(demographics,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(hbA1c,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(physical_individual_act,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(physical_act,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(plasma_fasting_insulin,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(sleep_data,left_on = "SEQN",right_on = "SEQN")

print(masterlist)



