# Cross-tabulation and heatmap for categorical vs categorical

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorical_main():
    labeled_selected_features = pd.read_csv('../../../../selected_features_labeled.csv', sep='\t')
    categorical_graph(labeled_selected_features)

def categorical_graph(labeled_selected_features):
    # iterate through the selected features and check whether feature is in continous_vars 
    # if feature is not in continous_vars, then it is categorical

    selected_vars = ['BPQ020', 'PADDURAT', 'SLD010H', 'LBXAPB', 'LBDINSI', 'LBXGH']

    continuous_vars = [col for col in selected_vars if col in labeled_selected_features.columns 
                    and labeled_selected_features[col].dtype in ['float64', 'int64'] 
                    and labeled_selected_features[col].nunique() > 10]

    categorical_vars = [col for col in selected_vars if col not in continuous_vars]

    #remove SEQN value
    del continuous_vars[0]

    # rename columns for better readability
    rename_dict = {
        'BPQ020': 'Blood Pressure',
        'PADDURAT': 'Physical Activity Duration',
        'SLD010H': 'Sleep Hours',
        'LBXAPB': 'Apolipoprotein B',
        'LBDINSI': 'Insulin Level',
        'LBXGH': 'Glycohemoglobin'
    }

    labeled_selected_features.rename(columns=rename_dict, inplace=True)
    renamed_vars = [rename_dict[col] for col in categorical_vars]


    if len(renamed_vars) == 1:
        cat_col = renamed_vars[0]
        
        # Bar plot of category counts
        plt.figure(figsize=(6, 4))
        sns.countplot(x=labeled_selected_features[cat_col], palette="coolwarm", hue=labeled_selected_features[cat_col], legend=False)
        plt.title(f"Distribution of {cat_col}")
        plt.xlabel(cat_col)
        plt.ylabel("Count")
        
        filename = f"visualization/{cat_col}_distribution.png"
        plt.savefig(filename)
        plt.show()
        
    else:
        for cat_col1 in renamed_vars:
            for cat_col2 in renamed_vars:
                if cat_col1 != cat_col2:
                    crosstab = pd.crosstab(labeled_selected_features[cat_col1], labeled_selected_features[cat_col2])
                    plt.figure(figsize=(5, 3))
                    sns.heatmap(crosstab, annot=True, cmap='coolwarm', fmt='d')
                    plt.title(f'{cat_col1} vs {cat_col2}')
                    filename = f"feature_specific/categoricalvs.categorical/visualization/{cat_col1}_vs_{cat_col2}.png"
                    plt.savefig(filename)
                    plt.close() 
                    plt.show()

if __name__ == "__main__":
    categorical_main()

