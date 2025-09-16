def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	tp = sum(1 for a, p in zip(y_true, y_pred) if a == 1 and p == 1 )
    fp = sum(1 for a, p in zip(y_true, y_pred) if a == 0 and p == 1 )
    fn = sum(1 for a, p in zip(y_true, y_pred) if a == 1 and p == 0 )
    tn = sum(1 for a, p in zip(y_true, y_pred) if a == 0 and p == 0 )

    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    precision = tp / (tp+fp) if (tp+fp) >0 else 0.0

    f1 = 2 * recall * precision / (recall + precision) if (recall + precision) else 0.0
	
	return round(f1,3)