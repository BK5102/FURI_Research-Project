# model selection using random forest 

from sklearn.ensemble  import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import common

def main():
    X_resampled, y_resampled, X_test_scaled, y_test = common.prepareData()
    accuracy = train_evaluate_model(X_resampled, y_resampled, X_test_scaled, y_test)
    return accuracy

def train_evaluate_model(X_resampled, y_resampled, X_test_scaled, y_test):
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_resampled, y_resampled)

    y_pred = rf_model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Random Forest Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))

    return accuracy

if __name__ == "__main__":
    main()
