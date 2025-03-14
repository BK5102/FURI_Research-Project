# model selection using logistic regression

from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import common

def main():
    X_resampled, y_resampled, X_test_scaled, y_test = common.prepareData()
    accuracy = train_evaluate_model(X_resampled, y_resampled, X_test_scaled, y_test)
    return accuracy

def train_evaluate_model(X_resampled, y_resampled, X_test_scaled, y_test):
    print("\nLogistic Regression:")
    log_reg = LogisticRegression(max_iter=2000, class_weight='balanced', random_state=42)
    log_reg.fit(X_resampled, y_resampled)

    y_pred = log_reg.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))

    return accuracy

if __name__ == "__main__":
    main()
