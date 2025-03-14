import pandas as pd
import numpy as np

## CHOLESTEORL - LDL, TRIGLYCERIDE & APOB

# LBXAPB (24 to 345 Range of Values)

def clean_cholesterol_ApoB(ApoB_level):
    # Replace known special codes with numeric or NaN
    ApoB_level = ApoB_level.replace({
        ".": np.nan,  # Missing
    })

    return ApoB_level