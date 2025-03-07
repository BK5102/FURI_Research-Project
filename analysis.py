# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import prepare_data, save_cleaned_data

def main():
    # 1. Get the cleaned data
    combined_selected_features = prepare_data()
    
    # 2. Save the cleaned dataset and stats
    save_cleaned_data(combined_selected_features, 
                      data_path="selected_features.csv", 
                      stats_path="selected_features_stats.csv")
    
    print("test line")
    
    """ # 3. Perform additional analysis or visualization
    numeric_cols = combined_selected_features.select_dtypes(include=[float, int]).columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(combined_selected_features[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show() """

if __name__ == "__main__":
    main()


""" # Determine which columns are numeric or categorical
numeric_cols = combined_selected_features.select_dtypes(include=[np.number]).columns

# Plot numeric distributions
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(combined_selected_features[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show() """

""" sns.countplot(x="BPQ020", data=BPC_df)
plt.title("Distribution of BPQ020 (High Blood Pressure)")
plt.xlabel("High Blood Pressure (2=No, 1=Yes)")
plt.ylabel("Count")
plt.show() """



