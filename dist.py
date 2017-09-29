import numpy as np

x = np.random.rand(1000, 3)
y = np.random.rand(1000, 3)

dist = np.sqrt(np.dot(x, x)) - (np.dot(x, y) + np.dot(x, y)) + np.dot(y, y)