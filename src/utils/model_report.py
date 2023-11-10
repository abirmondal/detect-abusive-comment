import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import seaborn as sns

def model_eval(y_test, y_pred) -> None:
    '''
    Prints the following Model Evaluation Metrices
    * Accuracy Score
    * Weighted Precision Score
    * Weighted Recall Score
    * F1-Score
    * Classification Report

    Args:
    * y_test(Numpy Array): Actual Labels
    * y_pred(Numpy Array): Predicted Labels

    Returns:
    None
    '''
    print('    Accuracy Score: ', metrics.accuracy_score(y_test, y_pred))
    print('Weighted Precision: ', metrics.precision_score(y_test, y_pred))
    print('   Weighted Recall: ', metrics.recall_score(y_test, y_pred))
    print('          F1-Score: ', metrics.f1_score(y_test, y_pred))
    print('\nClassification Report :-\n',
            metrics.classification_report(y_test, y_pred))
    
def confusion_mat(y_test, y_pred) -> None:
    '''
    Visualize Confusion Evaluation Matrix using Heatmap.

    Args:
    * y_test(Numpy Array): Actual Labels
    * y_pred(Numpy Array): Predicted Labels

    Returns:
    None
    '''
    confusion_matrix_sklearn = metrics.confusion_matrix(y_test, y_pred)
    sns.heatmap(confusion_matrix_sklearn, linewidths=0.2,
                annot=True, cmap='YlGnBu')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
