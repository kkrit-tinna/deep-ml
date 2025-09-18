import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    final_hidden_state = initial_hidden_state
    for x in input_sequence:
        final_hidden_state = np.tanh(np.dot(Wx, x) + np.dot(Wh, final_hidden_state) + b)
	return np.round(final_hidden_state, 4)