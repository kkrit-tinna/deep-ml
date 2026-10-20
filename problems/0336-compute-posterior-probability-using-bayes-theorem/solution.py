def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	# calculate joint probabilities
	joints = [p * l for p, l in zip(priors, likelihoods)]
	evidences = sum(joints)

	if evidences == 0:
		raise ValueError("Total probability of evidence is zero; posteriors are undefined.")
	
	post = []
	for j in joints:
		post.append(j / evidences)
	
	return post