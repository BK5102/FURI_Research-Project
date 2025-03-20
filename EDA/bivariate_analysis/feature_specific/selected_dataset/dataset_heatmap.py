#heatmap of complete dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    labeled_selected_features = pd.read_csv('../../../../selected_features_labeled.csv', sep='\t')
    selected_vars = ['BPQ020', 'PADDURAT', 'SLD010H', 'LBXAPB', 'LBDINSI', 'LBXGH']

    #display_heatmap(labeled_selected_features[selected_vars])
    # rename columns for better readability
    rename_dict = {
        'BPQ020': 'Blood Pressure',
        'PADDURAT': 'Physical Activity Duration', #continous
        'SLD010H': 'Sleep Hours',
        'LBXAPB': 'Apolipoprotein B',
        'LBDINSI': 'Insulin Level',
        'LBXGH': 'Glycohemoglobin'
    }

    labeled_selected_features = labeled_selected_features.rename(columns=rename_dict, inplace=False)
    renamed_vars = [rename_dict[col] for col in selected_vars]

    display_heatmap(labeled_selected_features[renamed_vars])

def display_heatmap(selected_data):
    plt.figure(figsize=(10,8))
    sns.heatmap(selected_data.corr(), cmap='coolwarm', annot=True, fmt='.2f')

    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)

    plt.suptitle("Correlation Matrix of selected features", fontsize=16)

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    print("test line")
    plt.savefig("visualizations/selected_features_correlation_matrix.png")

if __name__ == "__main__":
    main()
