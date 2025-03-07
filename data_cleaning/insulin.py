import pandas as pd
import numpy as np

## PLASMA FASTING GLUCOSE AND INSULIN

# LBDINSI

def clean_plasma_fasting_glucose_insulin(insulin_level_pmol_L):
    # Replace known special codes with numeric or NaN
    insulin_level_pmol_L = insulin_level_pmol_L.replace({
        ".": np.nan,  # Missing
    })
    return insulin_level_pmol_L
