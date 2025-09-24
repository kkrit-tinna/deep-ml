import numpy as np
import math
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	weights = initial_weights
	bias = initial_bias
	mse_values = []

	for _ in range(epochs):
		# calculate predictions & mse
		predictions = []
		for f_v in features:
			z = np.dot(weights, f_v) + bias
			prob = 1/(1 + math.exp(-z))
			predictions.append(prob)
		
		predictions = np.array(predictions)
		errors = predictions - labels
		mse = np.mean(errors**2)
		mse_values.append(np.round(mse, 4))

		# calculate gradients
		d_loss_d_pred = 2 * errors / len(labels) 
		d_pred_d_z = predictions * (1 - predictions)
		d_z_d_w = features
		d_z_d_b = 1

		d_losss_d_z = d_loss_d_pred * d_pred_d_z

		d_loss_d_w = np.dot(d_z_d_w.T, d_losss_d_z)
		d_loss_d_b = np.sum(d_z_d_b * d_losss_d_z)

		# update weights
		weights -= learning_rate * d_loss_d_w
		bias -= learning_rate * d_loss_d_b

	updat