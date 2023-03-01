import numpy as np

print("Début de la méthode du gradient conjugué")

def conjgrad(A, b, x):
    #defining variables that evaluate the solution
    r = b - A * x
    p = r
    rsold = np.dot(np.transpose(r),r)

    #start of main loop
    for i in range(1,len(b)):
        A_prime = A * p
        alpha = rsold / np.dot(np.transpose(p), A_prime)
        x = x + alpha * p
        r = r - alpha * A_prime
        rsnew = np.dot(np.transpose(r),r)

        #return value if rsnew is small enough
        if np.sqrt(rsnew) < 1e-10 :
            break
        p = r + (rsnew/rsold) * p
        rsold = rsnew
    return x




print("Fin de la méthode du gradient conjugué")

