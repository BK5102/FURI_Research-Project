# scatter plot of pairs of continous vs. continous variables

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def continous_main():
    labeled_selected_features = pd.read_csv('../../../../selected_features_labeled.csv', sep='\t')
    continous_graph(labeled_selected_features)

def continous_graph(labeled_selected_features):

    selected_vars = ['BPQ020', 'PADDURAT', 'SLD010H', 'LBXAPB', 'LBDINSI', 'LBXGH']


    continuous_vars = [col for col in selected_vars
                       if col in labeled_selected_features.columns]
    if not continuous_vars:
        print("No matching columns found in dataset.")
        return
    
    #remove SEQN value
    del continuous_vars[0]

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
    renamed_vars = [rename_dict[col] for col in continuous_vars]

    #plt.figure(figsize=(10,6))

    sns.pairplot(labeled_selected_features, vars=renamed_vars, hue='PreDM', diag_kind='kde')
    plt.suptitle("Pairplot of all continous variables in dataset", fontsize=12, y=1.03, ha='center')
    print("test line")
    plt.savefig("visualizations/pairplot_continous.png")
    
    #plt.show()

if __name__ == "__main__":
    continous_main()








