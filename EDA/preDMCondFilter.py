import pandas as pd
import os
from analysis_specific_main import main as analysis_main

#print("current working directory: ", os.getcwd())

def preDM_extract():
    combined_selected_features, preDM_criteria = analysis_main()

    preDMCondFilter(combined_selected_features, preDM_criteria)
    print('test line')


def preDMCondFilter(combined_selected_features, preDM_criteria):
    
    combined_selected_features.columns = combined_selected_features.columns.str.strip()

    combined_selected_features['Labels'] = preDM_criteria.astype(int)

    combined_selected_features.to_csv(r'..\spreadsheets_csv\selected_features_labeled.csv', sep='\t', index=True)

if __name__ == "__main__":
    preDM_extract()
#labeled column that distinguishes preDM vs. non preDM with 