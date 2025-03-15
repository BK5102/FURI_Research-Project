#heatmap of complete dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    labeled_selected_features = pd.read_csv('../../../selected_features_labeled.csv', sep='\t')
    display_heatmap(labeled_selected_features)

def display_heatmap(complete_dataset):
    plt.figure(figsize=(10,6))

    sns.heatmap(complete_dataset.corr(), cmap='coolwarm', annot=True, fmt='.2f')
    plt.title("Correlation Matrix of complete dataset", fontsize=10)
    print("test line")
    plt.savefig("visualizations/correlation_matrix.png")

if __name__ == "__main__":
    main()
