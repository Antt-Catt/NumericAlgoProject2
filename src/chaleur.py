import numpy as np
import random
from scipy import linalg
import matplotlib.pyplot as plt
import gradient as grd

#Main

def make_A(n):
    A = np.full((n**2, n**2), 0)
    for i in range(n**2):
        A[i][i] = -4
        if i % n != (n - 1):
            A[i + 1][i] = 1
            A[i][i + 1] = 1
        if (i + n) < n**2:
            A[i + n][i] = 1
            A[i][i + n] = 1
    return A

def central_radiator(N):
    F = np.zeros((N,N))
    for i in range(-1, 2):
        for j in range(-1, 2):
            F[N//2 + i][N//2 + j] = 100
    return map_to_vector(F,N)

def edge_heat_wall(N):
    F = np.zeros((N,N))
    for i in range(N):
        F[0][i] = 100
    return map_to_vector(F,N)

def central_heat_wall(N):
    F = np.zeros((N,N))
    for i in range(N):
        F[N//2][i] = 100
    return map_to_vector(F,N)

def X_radiator(N):
    F = np.zeros((N,N))
    for i in range(N):
        F[i][i] = 100
        F[i][N - i - 1] = 100
    return map_to_vector(F,N) 

def heat_map(N):
    A=make_A(N)
    F=central_radiator(N)

    x = np.linalg.solve(A,F)
    return vector_to_map(x,N)

#Tools

def vector_to_map(V, N):
    M = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            print(i, j)
            M[i, j] = V[i * N + j]
    return M

def map_to_vector(M, N):
    V = np.zeros(N*N)
    for i in range(N):
        for j in range(N):
            V[i * N + j] = M[i, j]
    return V

def display_heat_map(hm):
    plt.imshow(hm, cmap='jet')
    plt.colorbar()
    plt.show()

#Tests

n = 11

F = central_radiator(n)
result2 = grd.conjgrad(make_A(n), -F, np.full(n**2, 0))
display_heat_map(vector_to_map(F, n))
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

F = edge_heat_wall(n)
result2 = grd.conjgrad(make_A(n), -F, np.full(n**2, 0))
display_heat_map(vector_to_map(F, n))
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

F = central_heat_wall(n)
result2 = grd.conjgrad(make_A(n), -F, np.full(n**2, 0))
display_heat_map(vector_to_map(F, n))
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

F = X_radiator(n)
result2 = grd.conjgrad(make_A(n), -F, np.full(n**2, 0))
display_heat_map(vector_to_map(F, n))
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()
