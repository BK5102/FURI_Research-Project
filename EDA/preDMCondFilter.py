import pandas as pd

def main():
    combined_selected_features = pd.read_csv('../selected_features.csv', sep='\t')
    preDM_criteria = (combined_selected_features['LBDINSI'] >= 100) | (combined_selected_features['LBXAPB'] >= 110) | (combined_selected_features['LBXGH'] >= 5.5)

    preDMCondFilter(combined_selected_features, preDM_criteria)
    print('test line')


def preDMCondFilter(combined_selected_features, preDM_criteria):
    
    combined_selected_features.columns = combined_selected_features.columns.str.strip()

    combined_selected_features['PreDM'] = preDM_criteria.astype(int)

    combined_selected_features.to_csv('../selected_features_labeled.csv', sep='\t', index=False)
    


if __name__ == "__main__":
    main()