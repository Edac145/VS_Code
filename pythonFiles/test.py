import numpy as np

# Given data points
x_values = np.array([10.335, 8.995, 7.825])
y_values = np.array([1, 1/30, 1/60])

# Create the matrix A
A = np.vstack([x_values**3, x_values, np.ones_like(x_values)]).T

# Solve for coefficients using NumPy's linear algebra solver
coefficients = np.linalg.solve(A, y_values)

# Display the coefficients
a, c, d = coefficients
print(f'a: {a}, c: {c}, d: {d}')
