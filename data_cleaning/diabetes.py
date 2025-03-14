import pandas as pd
import numpy as np

## DIABETES 

# DID040
def clean_diab_age_column(age_diab):
    # Replace known special codes with numeric or NaN
    age_diab = age_diab.replace({
        666: 1,       # Less than 1 year
        777: np.nan,  # Refused
        999: np.nan,  # Don't know
        ".": np.nan
    })

    # clamp any values >85 to 85 (only if the data dictionary says "85" = "85 or older")
    age_diab.loc[age_diab > 85] = 85
    
    return age_diab

# DIQ230
def clean_diab_since_saw_specialist_column(how_long_since_saw_specialist):
     # Replace known special codes with numeric or NaN
    how_long_since_saw_specialist = how_long_since_saw_specialist.replace({
        1: 1,       # 1 year ago or less
        2:2,         # more than 1 year ago but no more than 2 years ago
        3:5,         # more than 2 years ago but no more than 5 years ago
        4:6,         # more than 5 years ago
        5: np.nan,  # Refused
        7: np.nan,  # Don't know
        9: np.nan,
        ".": np.nan,
    })
    
    return how_long_since_saw_specialist

# DIQ280
def clean_diab_last_A1C_level(last_A1C_level):
    # Replace known special codes with numeric or NaN
    last_A1C_level = last_A1C_level.replace({
        777: np.nan,  # Refused
        999: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return last_A1C_level

#DIQ220
def clean_diab_when_diagnosis(time_of_diagnosis):
    # Replace known special codes with numeric or NaN
    time_of_diagnosis = time_of_diagnosis.replace({
        1:3, # 3 months ago or less
        2:6, # more than 3 months ago, but no more than 6 months ago
        3:9, # more than 6 monghts ago, but no more than 9 months ago
        4:12, # more than 9 months ago, but no more than 12 months ago
        5:15, # more than 12 months ago, 
        7: np.nan, # Refused
        9: np.nan, # Don't Know
        ".": np.nan, # Missing

    })

    return time_of_diagnosis

# DID260
def clean_diab_how_often_check_blood_sugar(check_blood_sugar_val):
    # Replace known special codes with numeric or NaN
    check_blood_sugar_val = check_blood_sugar_val.replace({
        #0:1, 
        666: 0,
        777: np.nan,  # Refused
        999: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return check_blood_sugar_val

# DIQ300S
def clean_diab_systolic_blood_pressure_val(systolic_blood_pressure_val):
    # Replace known special codes with numeric or NaN
    systolic_blood_pressure_val = systolic_blood_pressure_val.replace({
        7777: np.nan,  # Refused
        9999: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return systolic_blood_pressure_val

# DIQ300D
def clean_diab_diastolic_blood_pressure_val(diastolic_blood_pressure_val):
    # Replace known special codes with numeric or NaN
    diastolic_blood_pressure_val = diastolic_blood_pressure_val.replace({
        7777: np.nan,  # Refused
        9999: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return diastolic_blood_pressure_val