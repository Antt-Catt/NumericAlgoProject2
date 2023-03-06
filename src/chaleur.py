import numpy as np
import random
from scipy import linalg
import matplotlib.pyplot as plt
import gradient as grd

#---------------Main---------------

#make_A : crée la matrice représentant l'opérateur Laplacien
#Entrée : n entier
#Sortie : A matrice (n**2)*(n**2) représentant l'opérateur Laplacien
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

#central_radiator : crée un vecteur représentant un carte ayant une source de chaleur centrale
#Entrée : N entier
#Sortie : vecteur N**2 représentant un carte ayant une source de chaleur centrale
def central_radiator(N):
    F = np.zeros((N,N))
    for i in range(-1, 2):
        for j in range(-1, 2):
            F[N//2 + i][N//2 + j] = 100
    return map_to_vector(F,N)

#edge_heat_wall : crée un vecteur représentant un carte ayant un mur de chaleur sur un côté
#Entrée : N entier
#Sortie : vecteur N**2 représentant un carte ayant un mur de chaleur sur un côté
def edge_heat_wall(N):
    F = np.zeros((N,N))
    for i in range(N):
        F[0][i] = 100
    return map_to_vector(F,N)

#central_heat_wall : crée un vecteur représentant un carte ayant un mur de chaleur au centre
#Entrée : N entier
#Sortie : vecteur N**2 représentant un carte ayant un mur de chaleur au centre
def central_heat_wall(N):
    F = np.zeros((N,N))
    for i in range(N):
        F[N//2][i] = 100
    return map_to_vector(F,N)

#X_radiator : crée un vecteur représentant un carte ayant des sources de chaleur sur les diagonales
#Entrée : N entier
#Sortie : vecteur N**2 représentant un carte ayant un mur des sources de chaleur sur les diagonales
def X_radiator(N):
    F = np.zeros((N,N))
    for i in range(N):
        F[i][i] = 100
        F[i][N - i - 1] = 100
    return map_to_vector(F,N)

#random_F : crée un vecteur représentant un carte ayant des sources de chaleur aléatoires
#Entrée : N entier
#Sortie : vecteur N**2 représentant un carte ayant un mur des sources de chaleur aléatoires
def random_F(N):
    F = np.zeros(N**2)
    for i in range(N**2):
        if random.randint(1, N) == 1:
            F[i] = 100
    return F


#---------------Tools---------------

#vector_to_map : retourne une matrice basée sur un vecteur
#Entrée : N entier, V vecteur de taille N**2
#Sortie : M matrice N*N telle que M[i][j] = V[i * N + j]
def vector_to_map(V, N):
    M = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            print(i, j)
            M[i, j] = V[i * N + j]
    return M

#map_to_vector : retourne un vecteur basé sur une matrice
#Entrée : N entier, M matrice de taille N*N
#Sortie : V vecteur de taille N**2 tel que V[i * N + j] = M[i][j]
def map_to_vector(M, N):
    V = np.zeros(N*N)
    for i in range(N):
        for j in range(N):
            V[i * N + j] = M[i, j]
    return V

#display_to_heat_map : affiche la carte de chaleur selon une matrice
#Entrée : hm matrice
#Sortie :
def display_heat_map(hm):
    plt.imshow(hm, cmap='jet')
    plt.colorbar()
    plt.show()

#---------------Tests---------------

#Taille des objets
n = 50

A = make_A(n)
x = np.full(n**2, 0)

#Résultat avec une source de chaleur centrale
F = central_radiator(n)
display_heat_map(vector_to_map(F, n))
result2 = grd.conjgrad(A, -F, x)
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

#Résultat avec un mur de chaleur sur un côté
F = edge_heat_wall(n)
display_heat_map(vector_to_map(F, n))
result2 = grd.conjgrad(A, -F, x)
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

#Résultat avec un mur de chaleur au centre
F = central_heat_wall(n)
display_heat_map(vector_to_map(F, n))
result2 = grd.conjgrad(A, -F, x)
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

#Résultat avec des sources de chaleur sur les diagonales
F = X_radiator(n)
display_heat_map(vector_to_map(F, n))
result2 = grd.conjgrad(A, -F, x)
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()

#Résultats avec des sources de chaleur aléatoires
F = random_F(n)
display_heat_map(vector_to_map(F, n))
result2 = grd.conjgrad(A, -F, x)
plt.imshow(vector_to_map(result2, n), cmap='jet')
plt.colorbar()
plt.show()
