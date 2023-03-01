import numpy as np
import math as math
from scipy import linalg

def conjgrad(A, b, x):
    r = b - np.dot(A, x)
    p = r
    rsold = np.dot(r.T, r)
    for i in range(len(b)):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p.T, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r.T, r)
        if np.sqrt(rsnew) < 1e-10:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return x

print(conjgrad(np.array([[2,3],[1,-2]]), np.array([[7],[11]]), np.array([[0],[0]])))
print(linalg.solve(np.array([[2,3],[1,-2]]), np.array([[7],[11]])))
