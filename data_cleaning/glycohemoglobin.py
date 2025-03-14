import pandas as pd
import numpy as np

## GLYCOHEMOGLOBIN

# LBXGH (3.8 to 15.6)

def clean_glycohemoglobin(glycohemoglobin_level_percent):
    # Replace known special codes with numeric or NaN
    glycohemoglobin_level_percent = glycohemoglobin_level_percent.replace({
        ".": np.nan,  # Missing
    })

    return glycohemoglobin_level_percent