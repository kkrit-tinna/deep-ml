
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
    tn = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 0)
	fp = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 1)
    fn = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 0)

    confusion_matrix = [[tp, fn], [fp, tn]]

    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0

    negativePredictive = tn / (tn + fn) if (tn + fn) > 0 else 0

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

