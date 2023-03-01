import numpy as np
import math as math
from scipy import linalg

def transpose(M):
    (n,m) = np.shape(M)
    B = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            B[j,i] = A[i,j]
    return B

def conjgrad(A, b, x):
    r = b - np.dot(A, x)
    p = r
    rsold = np.dot(r.T, r)
    for i in range(100):
        print(x)
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p.T, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r.T, r)
        if math.sqrt(rsnew) < 1e-10:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return x

print(conjgrad(np.array([[2,7],[1,-3]]), np.array([7,11]), np.array([0,0])))
print("sol = ", linalg.solve(np.array([[2,7],[1,-3]]), np.array([7,11])))
print(np.linalg.eigvals(np.array([[2,7],[1,-3]])))
print(conjgrad(np.array([[-4,1,0],[1,-4,1],[0,1,-4]]), np.array([7,11,1]), np.array([0,0,0])))
print("sol = ", linalg.solve(np.array([[-4,1,0],[1,-4,1],[0,1,-4]]), np.array([7,11,1])))

#def preconditioned_conjgrad(A, b, x):
    
