import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	output_height = ((input_height - kernel_height + padding * 2)//stride) + 1
    output_width = ((input_width - kernel_width + padding * 2)//stride) + 1

    output_matrix = np.zeros((output_height, output_width))

    padded_input = np.pad(input_matrix, ((padding, padding), (padding, padding)), mode='constant')

    for i in range(output_height):
        for j in range(output_width):
            curr_area = padded_input[i*stride: i*stride+kernel_height, j*stride: j*stride+kernel_width]
            output_matrix[i,j] = np.sum(curr_area*kernel)
    
	return output_matrix
