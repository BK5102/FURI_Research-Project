import decision_tree, logistic_regression, random_forest
import matplotlib.pyplot as plt

def get_accuracies():
    dt_accuracy = decision_tree.main()
    lr_accuracy = logistic_regression.main()
    rf_accuracy = random_forest.main()
    
    accuracies = {
        'Decision Tree': dt_accuracy,
        'Logistic Regression': lr_accuracy,
        'Random Forest': rf_accuracy
    }

    models = list(accuracies.keys())
    scores = list(accuracies.values())

    return models, scores

def display_accuracies():
    models, scores = get_accuracies()

    plt.figure(figsize=(10, 6))
    plt.barh(models, scores, color='olivedrab') # horizontal bar plot
    plt.xlabel('Accuracy')
    plt.title('Model Accuracies')
    plt.xlim(0, 1.1)  # x-axis limit from 0 to 1.1 to give some space for the bars
    plt.gca().invert_yaxis()  # display the highest accuracy at the top
    plt.show()

if __name__ == "__main__":
    display_accuracies()
    