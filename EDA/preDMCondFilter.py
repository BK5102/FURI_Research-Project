from analysis_specific_main import main as analysis_main

#print("current working directory: ", os.getcwd())

def preDM_extract():
    combined_selected_features, preDM_criteria = analysis_main()

    preDMCondFilter(combined_selected_features, preDM_criteria)
    print('test line')


def preDMCondFilter(combined_selected_features, preDM_criteria):
    
    combined_selected_features.columns = combined_selected_features.columns.str.strip()

    combined_selected_features['PreDM'] = preDM_criteria.astype(int)

    combined_selected_features.to_csv('../selected_features_labeled.csv', sep='\t', index=False)
    


if __name__ == "__main__":
    preDM_extract()
