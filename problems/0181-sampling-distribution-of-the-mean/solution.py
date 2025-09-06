import numpy as np

def simulate_clt(num_samples: int, sample_size: int, distribution: str = 'uniform') -> float:
	"""
	Simulate the Central Limit Theorem (CLT).

	Args:
		num_samples: number of repeated samples to draw
		sample_size: size of each sample
		distribution: 'uniform' or 'exponential'

	Returns:
		Mean of the sample means (float)
	"""
	# Your code here
    sample_means = []
    for _ in range(num_samples):
        if distribution == 'uniform':
            sample = np.random.uniform(0, 1, sample_size)
        elif distribution == 'exponential':
            sample = np.random.exponential(1, sample_size)
        else:
            raise ValueError("Invalid distribution type. Use 'uniform' or 'exponential'.")
        sample_means.append(np.mean(sample))
    return np.mean(sample_means)
    