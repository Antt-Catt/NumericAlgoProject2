from math import *
import numpy as np

def cholesky_fact(A):
    n,_ = np.shape(A)
    T = np.zeros((n,n))
    T[0][0] = A[0][0]
    for i in range(1,len(A)):
        s1 = 0 #somme du dessus
        for k in range(i):
            s1 += (T[i][k]**2)
        T[i][i] = math.sqrt(A[i][i] - s1)
        #----------------------#
        for j in range(i):
            s2 = 0 #somme du dessous
            for k in range(i):
                s2 += T[i][k]*T[j][k]
            T[j][i] = (A[i][j] - s2)/T[i][i]
    return np.transpose(T)
            
        
