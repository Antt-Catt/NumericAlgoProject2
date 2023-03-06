import numpy as np
import random
from scipy import linalg
import matplotlib.pyplot as plt
import gradient as grd

def make_A(n):
    A = np.zeros((n**2, n**2), int)
    for i in range(n**2):
        A[i][i] = -4
        if i % n != (n - 1):
            A[i + 1][i] = 1
            A[i][i + 1] = 1
        if (i + n) < n**2:
            A[i + n][i] = 1
            A[i][i + n] = 1
    return A


def make_F(n):
    return 100*np.random.rand(n**2)

n = 4

F = make_F(n)
print(F)
#plt.imshow(F, cmap='jet')
#plt.colorbar()
#plt.show()

result1 = linalg.solve(make_A(n), F)
result2 = grd.conjgrad(make_A(n), F, np.full(n**2, 1))
print(result1)
print(result2)
# plt.imshow(result2, cmap='jet')
# plt.colorbar()
# plt.show()
