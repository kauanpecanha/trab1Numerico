import numpy as np
from definitive import A, m21, m31, m41, m32, m42, m43

def LU_decomposition(A):
    """
    Realiza a fatoração LU de uma matriz A.
    
    Argumento:
    A: matriz de entrada
    
    Retorna:
    L: matriz triangular inferior
    U: matriz triangular superior
    """
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Fatoração LU
    for i in range(n):
        # Calcula os elementos da matriz U
        for k in range(i, n):
            soma = sum([L[i][j] * U[j][k] for j in range(i)])
            U[i][k] = A[i][k] - soma
        
        # Calcula os elementos da matriz L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Elemento diagonal é 1
            else:
                soma = sum([L[k][j] * U[j][i] for j in range(i)])
                L[k][i] = (A[k][i] - soma) / U[i][i]
    
    return L, U


L, U = LU_decomposition(A)

print("Matriz A:")
print(A)
print("Matriz L:")
print(L)
print("Matriz U:")
print(U)
