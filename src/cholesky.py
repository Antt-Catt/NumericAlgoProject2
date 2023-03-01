from math import*
import numpy as np
import random as rd

def cholesky_exp(A):
    n,_=np.shape(A)
    T=np.zeros((n,n))
    for j in range(n):
        sum1=0
        for k in range (1,j):
            sum1 += (T[j][k]**2)
        T[j][j]=sqrt(A[j][j]-sum1)
        i=0
        while (j>=i):
            sum2=0  
            for k in range (1,i):
                sum2 += T[i][k]*T[j][k]
            T[j][i]= (A[i][j]-sum2)/(T[i][i])
            i += 1
    return T

def sym_matrices_gen(n,x):
    S=np.zeros((n,n))
    while (x>0):
        i=rd.randint(n)
        j=rd.randint(n)
        if (S[i][j] == 0):
            S[i][j]=rd.randint(n)
            S[j][i]=S[i][j]
            x -= 1
    return S

def cholesky_incomp(A):
    n,_=np.shape(A)
    T=np.zeros((n,n))
    for j in range(n):
        if (A[j][j] != 0):
            sum1=0
            for k in range (1,j):
                sum1 += (T[j][k]**2)
            T[j][j]=sqrt(A[j][j]-sum1)
        i=0
        while (j>=i):
            if (T[j][i] != 0):
                sum2=0  
                for k in range (1,i):
                    sum2 += T[i][k]*T[j][k]
                T[j][i]= (A[i][j]-sum2)/(T[i][i])
                i += 1
    return T

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
print("Résultation pour implémentation :\n",cholesky_exp(A))
print("Résultation pour implémentation incomplète:\n",cholesky_exp(A))


