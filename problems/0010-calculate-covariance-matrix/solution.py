
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# initiate an empty vector for storage
	result = []
	# initiate a vector of means on all features
	mean_vectors = []
	for features in vectors:
		mean = sum(features)/len(features)
		mean_vectors.append(mean)
	# define covariance formula as mean of (v1-m1)*(v2-m2)
	def calc_cov(v1, v2, m1, m2):
		cov_sum = 0
		for x, y in zip(v1,v2):
			cov_sum += (x-m1)*(y-m2)
		cov = cov_sum/(len(v1)-1)
		return cov
	# apply covariance to each pair of X & Y
	for i in range(len(vectors)):
		covs = []
		for j in range(len(vectors)):
			cov = calc_cov(vectors[i], vectors[j], mean_vectors[i], mean_vectors[j])
			covs.append(cov)
		result.append(covs)

	return result


