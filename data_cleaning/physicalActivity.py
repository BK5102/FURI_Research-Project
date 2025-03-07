import pandas as pd
import numpy as np

## PHYSICAL ACTIVITY

# PAQ180
def clean_physAct_avg_level(avg_level_each_day):
    # Replace known special codes with numeric or NaN
    avg_level_each_day = avg_level_each_day.replace({
        1:1, 
        2:2,
        3:3,
        4:4,
        7: np.nan,  # Refused
        9: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return avg_level_each_day

## PHYSICAL ACTIVITY - INDIVIDUAL ACTIVITIES 

# PADDURAT
def clean_physAct_indiv_avg_duration(avg_duration):
    # Replace known special codes with numeric or NaN
    avg_duration = avg_duration.replace({
        1:1, 
        2:2,
        3:3,
        4:4,
        7: np.nan,  # Refused
        9: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return avg_duration
