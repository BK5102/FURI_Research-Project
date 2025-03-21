# analysis.py

    # preDM criteria:
    # plasma fasting insulin - LBDINSI
    # apob levels - LBXAPB
    # hba1c levels - LBXGH

import pandas as pd
import matplotlib.pyplot as plt
from preDM_visualization import preDM_visualization
from non_preDM_visualization import non_preDM_visualization

def main():
    # 1. Get the cleaned data
    combined_selected_features = pd.read_csv('../selected_features.csv', sep='\t')
    combined_selected_features.columns = combined_selected_features.columns.str.strip()

    # 2. Filter out data that meets preDM critera
    preDM_criteria = (combined_selected_features['LBDINSI'] >= 100) | (combined_selected_features['LBXAPB'] >= 110) | (combined_selected_features['LBXGH'] >= 5.5)
    preDM_filter = combined_selected_features[preDM_criteria]

    non_preDM_criteria = (combined_selected_features['LBDINSI'] < 100) | (combined_selected_features['LBXAPB'] < 110) | (combined_selected_features['LBXGH'] < 5.5)
    non_preDM_filter = combined_selected_features[non_preDM_criteria]

    # 3. Perform analysis or visualization
    preDM_visualization.preDM_visualization(preDM_filter)
    non_preDM_visualization.non_preDM_visualization(non_preDM_filter)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
     main()
