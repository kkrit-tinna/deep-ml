import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
	for feature in features:
        # calculate probs for each feature
        z = sum(w * x for w, x in zip(weights, feature)) + bias
        # log transform probs for binary classification
        probability = 1 / (1 + math.exp(-z))
        probabilities.append(probability)
    
    mse = sum((p - l)**2 for p, l in zip(probabilities, labels)) / len(labels)
	return probabilities, mse