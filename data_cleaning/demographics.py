import pandas as pd
import numpy as np

## DEMOGRAPHIC VARIABLES AND SAMPLE WEIGHTS

# RIDAGEMN
def clean_demographic_age(individual_age):
    # Replace known special codes with numeric or NaN
    individual_age = individual_age.replace({
        ".": np.nan,  # Missing
    })

    return individual_age
