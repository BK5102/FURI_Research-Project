# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import prepare_data, save_cleaned_data

def main():
    # 1. Get the cleaned data
    combined_selected_features = prepare_data()
    
    # Calculate mean exluding 0
    mean_without_zeros = combined_selected_features['LBDINSI'][combined_selected_features['LBDINSI'] != 0.0].mean().round(2)
    # Replace 0 with the calculated mean
    combined_selected_features['LBDINSI'] = combined_selected_features['LBDINSI'].replace(0.0, mean_without_zeros)

    mean_without_zeros = combined_selected_features['LBXAPB'][combined_selected_features['LBXAPB'] != 0.0].mean().round(2)
    combined_selected_features['LBXAPB'] = combined_selected_features['LBXAPB'].replace(0.0, mean_without_zeros)

    mean_without_zeros = combined_selected_features['LBXGH'][combined_selected_features['LBXGH'] != 0.0].mean().round(2)
    combined_selected_features['LBXGH'] = combined_selected_features['LBXGH'].replace(0.0, mean_without_zeros)

    mean_without_zeros = combined_selected_features['PADDURAT'][combined_selected_features['PADDURAT'] != 0.0].mean().round(2)
    combined_selected_features['PADDURAT'] = combined_selected_features['PADDURAT'].replace(0.0, mean_without_zeros)

    combined_selected_features['SLD010H'].fillna(0)
    mean_without_zeros = combined_selected_features['SLD010H'][combined_selected_features['SLD010H'] != 0.0].mean().round(2)
    combined_selected_features['SLD010H'] = combined_selected_features['SLD010H'].replace(0.0, mean_without_zeros)

    # 2. Save the cleaned dataset and stats
    save_cleaned_data(combined_selected_features, 
                      data_path="selected_features.csv", 
                      stats_path="selected_features_stats.csv")


if __name__ == "__main__":
    main()




