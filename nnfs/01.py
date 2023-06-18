import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [0.7, 0.2, 0.1, 0.9]]
bias = [2, 3, 0.5]

outputs = np.dot(weights, inputs) + bias

print(outputs)
