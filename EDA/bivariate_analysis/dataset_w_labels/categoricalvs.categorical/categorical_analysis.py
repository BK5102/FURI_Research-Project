# Cross-tabulation and heatmap for categorical vs categorical

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorical_main():
    labeled_selected_features = pd.read_csv('../../../selected_features_labeled.csv', sep='\t')
    categorical_graph(labeled_selected_features)

def categorical_graph(labeled_selected_features):
    # iterate through entire dataset and check whether feature is in continous_vars 
    # if feature is not in continous_vars, then it is categorical
    continuous_vars = [col for col in labeled_selected_features.columns 
                       if labeled_selected_features[col].dtype in ['float64', 'int64'] and labeled_selected_features[col].nunique() > 10]
    categorical_vars = [col for col in labeled_selected_features.columns if col not in continuous_vars]
    categorical_data = labeled_selected_features[categorical_vars]

    for cat_col1 in categorical_data:
        for cat_col2 in categorical_data:
            if cat_col1 != cat_col2:
                crosstab = pd.crosstab(categorical_data[cat_col1], categorical_data[cat_col2])
                plt.figure(figsize=(5, 3))
                sns.heatmap(crosstab, annot=True, cmap='coolwarm', fmt='d')
                plt.title(f'{cat_col1} vs {cat_col2}')
                filename = f"visualizations/{cat_col1}_vs_{cat_col2}.png"
                plt.savefig(filename)
                plt.close() 
                plt.show()

if __name__ == "__main__":
    categorical_main()

