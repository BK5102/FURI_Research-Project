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
    
    # 3. Perform additional analysis or visualization
    visualization_of_data(combined_selected_features)

def visualization_of_data(combined_selected_features):
    independent_vars = ['LBDINSI']
                        #'BPQ020'
                        #'DIQ010', 'DIQ190A', 'DIQ190B', 'PAQ180', 'PADACTIV', 'PADDURAT', 
                        #'SLD010H', 'LBXAPB', 'LBDINSI', 'LBXGH']
    dependent_var_gender = 'RIAGENDR'
    dependent_var_age = 'RIDAGEMN'

    numeric_cols = combined_selected_features[independent_vars].select_dtypes(include=[float, int]).columns

    #Distribution of independent variables by gender
    for col in numeric_cols:
        #bins = range(1,11)
        plt.figure(figsize=(8, 4))
        sns.histplot(data=combined_selected_features, x=col, hue=dependent_var_gender, kde=True, palette="coolwarm", alpha=0.6, bins=8)
        #plt.ylim(0, 1000)

        plt.xticks(fontsize=8)
        plt.title(f"Distribution of {col} by {dependent_var_gender}")
        plt.ylabel("Frequency")
        plt.legend(title="Gender", labels=["Male", "Female"])
        
        #plt.xticks(bins)

        plt.tight_layout()
        plt.show()


    #Distribution of independent variables by age
    """ for col in numeric_cols:
        #bins = range(1,11)
        plt.figure(figsize=(8, 4))
        sns.histplot(data=combined_selected_features, x=col, y=dependent_var_age, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
        plt.title(f"Regression Plot of {col} vs Age (in months)")
        plt.show() """


if __name__ == "__main__":
    main()




