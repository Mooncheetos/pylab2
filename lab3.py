import numpy as np


def kram(A, B):
    D = np.linalg.det(A)
    m = len(A)
    r = list()
    for i in range(m):
        Dj = np.copy(A)
        Dj[:, i] = B
        r.append(np.linalg.det(Dj / D))
    return r


A = [
    [0.92, 0.03, 0, 0.04],
    [0, 0.69, -0.27, 0.08],
    [0.11, 0, -0.03, 0.42],
    [-0.33, 0, 1.07, -0.21],
]
B = [1.2, -0.81, -0.17, 0.92]
X = kram(A, B)
print("X =", X)
