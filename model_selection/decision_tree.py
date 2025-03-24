# model selection using decision tree

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import plot_tree
import common_copy
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    X_train, X_test, X_test_scaled, y_test = common_copy.prepareData()
    accuracy = train_evaluate_model(X_train, X_test, X_test_scaled, y_test)
    return accuracy

def train_evaluate_model(X_train, X_test, X_test_scaled, y_test):
    """ dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, X_test) """

    dt_model = 



    y_pred = dt_model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Decision Tree Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))

    return accuracy

if __name__ == "__main__":
    main()
