import pandas as pd
import numpy as np

## SLEEP

# SLD010H (1 to 11)
def clean_sleep_amount_of_sleep(hours_of_sleep):
     # Replace known special codes with numeric or NaN
    hours_of_sleep = hours_of_sleep.replace({
        12:12, 
        77: np.nan,  # Refused
        99: np.nan,  # Don't know
        ".": np.nan,  # Missing
    })

    return hours_of_sleep
