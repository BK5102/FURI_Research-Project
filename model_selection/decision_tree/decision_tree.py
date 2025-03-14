# model selection using decision tree

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer

def main():
    labeled_selected_features = pd.read_csv('../../../selected_features_labeled.csv', sep='\t', header=0)

    X_train, X_test, y_train, y_test = encode_and_split(labeled_selected_features)

    X_train_scaled, X_test_scaled = scaleFeatures(X_train, X_test)

    # oversample the minority class using SMOTE
    # avoid overfitting
    # improves performance on imbalanced datasets
    X_resampled, y_resampled = handle_class_imbalance(X_train_scaled, y_train)

    train_evaluate_model(X_resampled, y_resampled, X_test_scaled, y_test)

def encode_and_split(labeled_selected_features):
    #imp = SimpleImputer(missing_values=np.nan, strategy='mean') 

    #X = labeled_selected_features[['BPQ020', 'PADDURAT', 'SLD010H', 'RIAGENDR', 'LBXAPB', 'LBDINSI', 'LBXGH']]
    X = labeled_selected_features[['BPQ020', 'PADDURAT', 'RIAGENDR', 'LBXAPB', 'LBDINSI', 'LBXGH']]

    #imp = imp.fit(X)
    #X = imp.transform(X)

    Y = labeled_selected_features["PreDM"].copy()
    #Y = Y.apply(lambda x: 1 if x == 1 else 0 if x == 2 else None)
        # 1 for haspreDM, 0 for does not have preDM, None for other values(like 3)
    #Y = Y.dropna()  # Remove rows with NaN values
   
    X = X.loc[Y.index]

    #X = X.loc[Y.index].copy() #Make sure to copy, to avoid slice issues.
    #X = X.drop("PreDM", axis=1) #Remove the target variable from X

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print(y_train.nunique)

    return X_train, X_test, y_train, y_test

def scaleFeatures(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Handle NaNs introduced by StandardScaler
    #X_train_scaled = np.nan_to_num(X_train_scaled)
    #X_test_scaled = np.nan_to_num(X_test_scaled)

    return X_train_scaled, X_test_scaled

def handle_class_imbalance(X_train_scaled, y_train):
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)

    return X_resampled, y_resampled

def train_evaluate_model(X_resampled, y_resampled, X_test_scaled, y_test):
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_resampled, y_resampled)

    y_pred = dt_model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Decision Tree Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
