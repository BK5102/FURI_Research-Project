import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#from imblearn.over_sampling import SMOTE

def prepareData():
    labeled_selected_features = pd.read_csv('../selected_features_labeled.csv', sep='\t', header=0)

    X_train, X_test, y_train, y_test = encode_and_split(labeled_selected_features)

    X_train_scaled, X_test_scaled = scaleFeatures(X_train, X_test)
 
    #X_resampled, y_resampled = handle_class_imbalance(X_train_scaled, y_train)

    return X_train, X_test, X_test_scaled, y_test

def encode_and_split(labeled_selected_features):

    #X = labeled_selected_features[['BPQ020', 'PADDURAT', 'SLD010H', 'RIAGENDR', 'LBXAPB', 'LBDINSI', 'LBXGH']]
    X = labeled_selected_features[['BPQ020', 'PADDURAT',  'SLD010H']]
    Y = labeled_selected_features["PreDM"].copy()
   
    X = X.loc[Y.index]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, train_size=0.7, random_state=42)

    return X_train, X_test, y_train, y_test

def scaleFeatures(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled

# oversample the minority class using SMOTE
# avoid overfitting
# improves performance on imbalanced datasets

""" def handle_class_imbalance(X_train_scaled, y_train):
    smote = SMOTE(random_state=42) ## removal of SMOTE
    X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

    return X_resampled, y_resampled """