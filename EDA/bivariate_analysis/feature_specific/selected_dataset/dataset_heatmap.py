#heatmap of complete dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    labeled_selected_features = pd.read_csv('../../../../selected_features_labeled.csv', sep='\t')
    selected_vars = ['BPQ020', 'PADDURAT', 'SLD010H', 'LBXAPB', 'LBDINSI', 'LBXGH']
    display_heatmap(labeled_selected_features[selected_vars])

def display_heatmap(selected_data):
    plt.figure(figsize=(10,6))

    sns.heatmap(selected_data.corr(), cmap='coolwarm', annot=True, fmt='.2f')
    plt.title("Correlation Matrix of selected features", fontsize=10)
    print("test line")
    plt.savefig("visualizations/selected_features_correlation_matrix.png")

if __name__ == "__main__":
    main()
