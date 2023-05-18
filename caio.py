import numpy as np
from index import A, m21, m31, m41, m32, m42, m43

def LU_decomposition(A):
    """
    Realiza a fatoração LU de uma matriz A.
    
    Args:
    A: matriz de entrada
    
    Returns:
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


# A = np.array([[2.94, 2.87, 2.33, 0],
#               [1.48, 2.45, 2.89, -1.23],
#               [6.31, 7.07, 2.79, 7.77],
#               [8.27, -8.69, 8.79, -1.79]])



L, U = LU_decomposition(A)

L[1][0] = m21
L[2][0] = m31
L[3][0] = m41

L[2][1] = m32
L[3][1] = m42

L[3][2] = m43

print("Matriz A:")
print(A)
print("Matriz L:")
print(L)
print("Matriz U:")
print(U)
