# scatter plot of pairs of continous vs. continous variables

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def continous_main():
    labeled_selected_features = pd.read_csv('../../../selected_features_labeled.csv', sep='\t')
    continous_graph(labeled_selected_features)

def continous_graph(labeled_selected_features):
    continuous_vars = [col for col in labeled_selected_features.columns 
                       if labeled_selected_features[col].dtype in ['float64', 'int64'] and labeled_selected_features[col].nunique() > 10]
    #remove SEQN value
    del continuous_vars[0]
    
    plt.figure(figsize=(10,6))

    sns.pairplot(labeled_selected_features, vars=continuous_vars, hue='PreDM', diag_kind='kde')
    plt.title("Pairplot of all continous variables in dataset", fontsize=10)
    print("test line")
    plt.savefig("visualizations/pairplot_continous.png")
    
    plt.show()

if __name__ == "__main__":
    continous_main()








