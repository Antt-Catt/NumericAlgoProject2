from math import*
import numpy as np
import random as rd

def cholesky_comp(A):
    n = A.shape[0]
    T = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            s = sum(T[i,k]*T[j,k] for k in range(j))
            T[i,j] = (A[i,j] - s) / T[j,j]
        s = sum(T[i,k]**2 for k in range(i))
        T[i,i] = np.sqrt(A[i,i] - s)
    
    return T

def sym_defpos_matrices_gen(n,k):
    # Matrice aléatoire avec environ k éléments non nuls
    A = np.random.randint(1,10, size=(n,n))
    for l in range(n*n-k):
        i=rd.randint(0,n-1)
        j=rd.randint(0,n-1)
        A[i][j]=0
        A[j][i]=0

    # Matrice symétrique
    A = 0.5 * (A + A.transpose())

    # Diagonale dominante
    for i in range(n):
        if (A[i][i]==0):
            A[i][i]=sum(A[j][i] for j in range(n))+1

    # Définie positive
    A = A.dot(A.transpose())

    return A


def cholesky_incomp(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1):
            s = A[i, j] - np.dot(L[i, :j], L[j, :j])
            if i == j:
                L[i, j] = np.sqrt(s)
            else:
                L[i, j] = s / L[j, j]
    return L

## Matrice A d'exemple pour tester Cholesky complète
A=np.zeros((4,4))
for i in range (4):
    A[i][0]=1
    A[0][i]=1
for i in range (1,4):
    A[i][1]=5
    A[1][i]=5
A[3][3]=15
A[2][2]=14
A[3][2]=14
A[2][3]=14


print("Matrice de test :\n",A,"\n")
print("Résultat théorique :\n",np.linalg.cholesky(A),"\n")
print("Résultation pour implémentation :\n",cholesky_comp(A))
C=sym_defpos_matrices_gen(5,5)
print("Génération matrice symétrique creuse:\n",C)
print("Résultat théorique :\n",np.linalg.cholesky(C),"\n")
print("Résultation pour implémentation incomplète:\n",cholesky_incomp(C))

##--------------------------Conditionnement------------------------

# A est la matrice à préconditionner
# T est la matrice de la factorisation de Cholesky complète de A

T=cholesky_comp(A)

# Matrice préconditionnée
M_1 = np.linalg.inv(T.T) @ np.linalg.inv(T)

# Conditionnement de A
cond_A = np.linalg.cond(A)

# Conditionnement de la matrice préconditionnée
cond_M_1 = np.linalg.cond(M_1 @ A)

# Comparaison des conditionnements
if cond_M_1 < cond_A:
    print("La matrice préconditionnée est de bonne qualité.")
else:
    print("La matrice préconditionnée est de mauvaise qualité.")


# A est la matrice à préconditionner
# T est la matrice de la factorisation de Cholesky incomplète de A

T=cholesky_incomp(A)

# Matrice préconditionnée
M_2 = np.linalg.inv(T.T) @ np.linalg.inv(T)

# Conditionnement de A
cond_A = np.linalg.cond(A)

# Conditionnement de la matrice préconditionnée
cond_M_2 = np.linalg.cond(M_2 @ A)

# Comparaison des conditionnements
if cond_M_2 < cond_A:
    print("La matrice préconditionnée est de bonne qualité.")
else:
    print("La matrice préconditionnée est de mauvaise qualité.")

if cond_M_1 < cond_M_2:
    print("Le conditionnement est meilleur avec la factorisation de Cholesky complète")
else:
    print("Le conditionnement est meilleur avec la factorisation de Cholesky incomplète")
