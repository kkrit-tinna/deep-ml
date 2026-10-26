import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	if len(data) == 0:
		return {'cleaned_data': [], 'outlier_indices': [], 'lower_bound': None, 'upper_bound': None}
	
	arr = np.array(data, dtype=float)
	q1, q3 = np.percentile(arr, [25, 75])
	iqr = q3 - q1
	lower = q1 - k*iqr
	upper = q3 + k*iqr

	is_outlier = ((arr < lower) | (arr > upper))
	
	return {'cleaned_data': [
		round(float(x), 4) for x in arr[~is_outlier]
	], 'outlier_indices': [
		int(i) for i in np.where(is_outlier)[0]
	], 'lower_bound': 
		round(float(lower), 4), 
		'upper_bound':
		round(float(upper), 4) }
