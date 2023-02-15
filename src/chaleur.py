import numpy as np

def make_A(n):
    A = np.zeros((n**2, n**2), int)
    # for j in range(n):
    #     for i in range(j * n, (j + 1) * n):
    #         A[i][i] = -4
    #         #if i != ((j * n) - 1):
    #         #    A[i + 1][i] = 1
    #         #    A[i][i + 1] = 1
    for i in range(n**2):
        A[i][i] = -4
        if i % n != (n - 1):
            A[i + 1][i] = 1
            A[i][i + 1] = 1
        if (i + n) < n**2:
            A[i + n][i] = 1
            A[i][i + n] = 1
    return A

print(make_A(4))
