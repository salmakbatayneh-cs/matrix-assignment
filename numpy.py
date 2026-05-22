import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

c = np.array([
    [5],
    [6]
])

print(a + b)

print(np.dot(a, b))

print(np.linalg.det(a))

print(np.linalg.inv(a))

print(np.linalg.solve(a, c))
