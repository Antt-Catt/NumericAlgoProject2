import numpy as np
import math as math
import cholesky as cly
import matplotlib.pyplot as plt

# conjgrad : résolution d'un système linéaire
# Entrée : A matrice n*n définie positive, b et x vecteurs 1*n
# Sortie : x tel que Ax = b
def conjgrad(A, b, x):
    r = b - np.dot(A, x)
    p = r
    rsold = np.dot(r.T, r)
    rsarray = [rsold]
    
    for i in range(5*len(b)):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p.T, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r.T, r)
        rsarray.append(rsnew)
        if math.sqrt(rsnew) < 1e-10:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew
        
    # plt.plot(rsarray)
    # plt.xlabel("Itérations")
    # plt.ylabel("Résidus")
    # plt.title("Résidus de la méthode du gradient conjugué sans préconditionneur")
    #plt.show()

    return x

print("Tests de conjgrad sans préconditionneur :")
## Les matrices Ak sont définies positives
# Premier test avec un système à 2 équations
print("2 équations :")
A1 = np.random.rand(2, 2)
A1 = np.dot(A1, A1.T)
#A1 = np.array([[3,1],[1,2]])
B1 = np.random.rand(2)
print(conjgrad(A1, B1, np.full((2), 0)), "obtenu")
print(np.linalg.solve(A1, B1), "attendu")

# Second test avec un système à 3 équations
print("3 équations :")
A2 = np.random.rand(3, 3)
A2 = np.dot(A2, A2.T)
B2 = np.random.rand(3)
print(conjgrad(A2, B2, np.full((3), 0)), "obtenu")
print(np.linalg.solve(A2, B2), "attendu")

# Troisième test avec un système à 5 équations
print("5 équations :")
A3 = np.random.rand(5, 5)
A3 = np.dot(A3, A3.T)
B3 = np.random.rand(5)
print(conjgrad(A3, B3, np.full((5), 0)), "obtenu")
print(np.linalg.solve(A3, B3), "attendu")

# Dernier test avec un système à 50 équations
print("50 équations :")
A4 = np.random.rand(50, 50)
A4 = np.dot(A4, A4.T)
B4 = np.random.rand(50)
print(conjgrad(A4, B4, np.full((50), 0)), "obtenu")
print(np.linalg.solve(A4, B4), "attendu")

#---------------Avec préconditionneur---------------

# conjgrad : résolution d'un système linéaire en prenant en compte un préconditionneur
# Entrée : A et M matrices n*n définies positives, b et x vecteurs 1*n
# Sortie : x tel que Ax = b
def precond_conjgrad(A, b, x, M):
    if M is None:
        M = np.identity(len(A))

    r = b - np.dot(A, x)
    z = np.linalg.solve(M, r)
    p = z
    rsold = np.dot(r.T, z)
    rsarray = [rsold]

    for i in range(25*len(b)):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p.T, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        z = np.linalg.solve(M, r)
        rsnew = np.dot(r.T, z)
        rsarray.append(rsnew)
        if np.sqrt(rsnew) < 1e-10:
            break
        p = z + (rsnew / rsold) * p
        rsold = rsnew

    # plt.plot(rsarray)
    # plt.xlabel("Itérations")
    # plt.ylabel("Résidus")
    # plt.title("Résidus de la méthode du gradient conjugué avec préconditionneurs")
    # plt.show()
    
    return x

print("Tests de conjgrad avec préconditionneur :")
## Les matrices Ak sont définies positives
## Les préconditionneurs Mk sont obtenus de la même manière que dans la partie précédente
# Premier test avec un système à 2 équations
print("2 équations :")
T1 = cly.cholesky_incomp(A1)
M1 = np.linalg.inv(T1.T) @ np.linalg.inv(T1)
print(precond_conjgrad(A1, B1, np.full((2), 0), M1), "obtenu")
print(np.linalg.solve(A1, B1), "attendu")

# Deuxième test avec un système à 3 équations
print("3 équations :")
T2 = cly.cholesky_incomp(A2)
M2 = np.linalg.inv(T2.T) @ np.linalg.inv(T2)
print(precond_conjgrad(A2, B2, np.full((3), 0), M2), "obtenu")
print(np.linalg.solve(A2, B2), "attendu")

# Troisième test avec un système à 5 équations
print("5 équations :")
T3 = cly.cholesky_incomp(A3)
M3 = np.linalg.inv(T3.T) @ np.linalg.inv(T3)
print(precond_conjgrad(A3, B3, np.full((5), 0), M3), "obtenu")
print(np.linalg.solve(A3, B3), "attendu")

# Dernier test avec un système à 50 équations
print("50 équations :")
T4 = cly.cholesky_incomp(A4)
M4 = np.linalg.inv(T4.T) @ np.linalg.inv(T4)
print(precond_conjgrad(A4, B4, np.full((50), 0), M4), "obtenu")
print(np.linalg.solve(A4, B4), "attendu")
