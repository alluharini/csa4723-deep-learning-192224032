import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
class1 = np.random.randn(50, 2) + [2, 2]
class2 = np.random.randn(50, 2) + [-2, -2]

plt.scatter(class1[:, 0], class1[:, 1], color='r', label='Class 1')
plt.scatter(class2[:, 0], class2[:, 1], color='b', label='Class 2')

x_values = np.linspace(-4, 4, 100)
y_values = x_values
plt.plot(x_values, y_values, color='k', linestyle='--')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
