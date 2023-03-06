import numpy as np
import matplotlib.pyplot as plt
"""
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
"""

#Tools

def vector_to_map(V, N):
    M = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            M[i, j] = V[i * N + j]
    return M

def map_to_vector(M, N):
    V = np.zeros((N*N, 1))
    for i in range(N):
        for j in range(N):
            V[i * N + j] = M[i, j]
    return V





#Main

def make_A(N):
    A = np.zeros((N*N, N*N))

    for i in range(N*N):
        for j in range(N*N):
            if (i==j):
                A[i, j] = -4
            elif (j == i+1):
                A[i, i+1] = 1
                A[i+1, i] = 1
            elif (j == i+N):
                A[i, i+N] = 1
                A[i+N, i] = 1
        if (i !=0 and i%N == 0):
            A[i, i-1] = 0
            A[i-1, i] = 0
    
    return A


def central_radiator(N):
    F = np.zeros((N,N))
    F[N//2][N//2] = 50
    return map_to_vector(F,N)

def heat_map(N):
    A=make_A(N)
    F=central_radiator(N)

    x = np.linalg.solve(A,F)
    return vector_to_map(x,N)



    


def display_heat_map(hm):
    fig, ax = plt.subplots()
    im = ax.imshow(-hm, cmap=plt.get_cmap('hot'))
    plt.axis('off')
    plt.show()