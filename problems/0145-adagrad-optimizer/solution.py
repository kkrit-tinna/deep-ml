import numpy as np

def adagrad_optimizer(parameter, grad, G, learning_rate=0.01, epsilon=1e-8):
    """
    Update parameters using the Adagrad optimizer.
    Adapts the learning rate for each parameter based on the historical gradients.
    Args:
        parameter: Current parameter value
        grad: Current gradient
        G: Accumulated squared gradients
        learning_rate: Learning rate (default=0.01)
        epsilon: Small constant for numerical stability (default=1e-8)
    Returns:
        tuple: (updated_parameter, updated_G)
    """
    # array inputs handling
    parameter = np.asarray(parameter, dtype=float)
    grad = np.asarray(grad, dtype=float)
    G = np.asarray(G, dtype=float)

    # validate inputs
    if learning_rate <= 0:
        raise ValueError("Learning rate must be positive")
    if epsilon <= 0:
        raise ValueError("Epsilon must be positive")
    if parameter.shape != grad.shape or parameter.shape != G.shape:
        raise ValueError("Parameter, grad, and G must all have the same shape")

    # compute & update parameter & G
    G = G + grad**2
    parameter = parameter - learning_rate * grad / (np.sqrt(G) + epsilon)

    return np.round(parameter, 5), np.round(G, 5)