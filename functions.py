import numpy as np
import matplotlib.pyplot as plt

# função para impressão da matriz
def printMatrix(matrix):
    
    for i in range(0, 4):
        for j in range(0, 5):
            if(j == 4):
                print(f'{matrix[i][j]:.2f} ')
            else:
                print(f'{matrix[i][j]:.2f} ', end='')

def printLUMatrix(matrix):

    for i in range(0, 4):
        for j in range(0, 4):
            if (j == 3):
                print(f'{matrix[i][j]:.2f} ')
            else:
                print(f'{matrix[i][j]:.2f} ', end='')


# função para permutar linhas
def swapPositions(matrix, linhapivotal, linhatrocar):
    aux = matrix[linhapivotal].copy()
    matrix[linhapivotal] = matrix[linhatrocar]
    matrix[linhatrocar] = aux

    return matrix

def determinePivot(matrix, column):
    
    pivot = 0
    i = 0
    
    if column == 0:


        for i in range(0, 4):
            
            if(pivot<matrix[i][column]):
                
                pivot=matrix[i][column]
                linhapivotal = i
            
    elif column == 1:

        for i in range(1, 4):
            
            if(pivot<matrix[i][column]):
                pivot=matrix[i][column]
                linhapivotal = i
    
    elif column == 2:

        for i in range(2, 4):
            if(pivot<matrix[i][column]):
                pivot = matrix[i][column]
                linhapivotal = i
    
    return [pivot, linhapivotal]

def zeroElementsBelow(matrix, pivot, column):
    
    if(column == 0):
        
        m21 = -((matrix[1][0])/pivot)
        m31 = -((matrix[2][0])/pivot)
        m41 = -((matrix[3][0])/pivot)

        # matrix[1, :] = matrix[1, :] + matrix[0, :] * m21
        # matrix[2, :] = matrix[2, :] + matrix[0, :] * m31
        # matrix[3, :] = matrix[3, :] + matrix[0, :] * m41

        for i in range(1, 4):
            for j in range(0, 5):
                
                if(i == 1):
                    matrix[i][j] = matrix[i][j] + matrix[i-1][j] * m21
                elif(i == 2):
                    matrix[i][j] = matrix[i][j] + matrix[i-2][j] * m31
                elif(i==3):
                    matrix[i][j] = matrix[i][j] + matrix[i-3][j] * m41

        # matrix[1][0] = 'm21'
        # matrix[2][0] = 'm31'
        # matrix[3][0] = 'm41'

        return [matrix, m21, m31, m41]
    
    elif(column == 1):
        
        m32 = -((matrix[2][1])/pivot)
        m42 = -((matrix[3][1])/pivot)

        # matrix[2, :] = matrix[2, :] + matrix[1, :] * m32
        # matrix[3, :] = matrix[3, :] + matrix[1, :] * m42

        for i in range(2, 4):
            for j in range(1, 5):
                
                if(i == 2):
                    matrix[i][j] = matrix[i][j] + matrix[i-1][j] * m32
                elif(i==3):
                    matrix[i][j] = matrix[i][j] + matrix[i-2][j] * m42


        # matrix[2][1] = 'm32'
        # matrix[3][1] = 'm42'
        
        return [matrix, m32, m42]
    
    elif(column == 2):

        m43 = -((matrix[3][2])/pivot)

        # matrix[3, :] = matrix[3, :] + matrix[2, :] * m43

        for i in range(3, 4):
            for j in range(2, 5):
                
                if(i==3):
                    matrix[i][j] = matrix[i][j] + matrix[i-1][j] * m43


        # matrix[3][2] = 'm43'

        return [matrix, m43]

def createLMatrix(matrix):
    n = len(matrix)
    L = np.zeros((n, n))

    for i in range(0, 4):
        for j in range(0, 4):
            if(i == j):
                L[i][j] = 1
    return L

def createUMatrix(matrix):
    n = len(matrix)
    U = np.zeros((n, n))

    for i in range(0, 4):
        for j in range(0, 4):

            if(i==0):
                U[i][j] = matrix[i][j]
            if(i==1):
                if(j==0):
                    continue
                else:
                    U[i][j] = matrix[i][j]
            if(i==2):
                if(j in range(0, 2)):
                    continue
                else:
                    U[i][j] = matrix[i][j]
            if(i==3):
                if(j in range(0, 3)):
                    continue
                else:
                    U[i][j] = matrix[i][j]

    return U

def defineLElements(matrix, L, column):
    if(column == 0):
        for i in range(1, 4):
            L[i][column] = matrix[i][column]

    if(column == 1):
        for i in range(1, 4):
            L[i][column-1] = matrix[i][column-1]
        
        for i in range(2, 4):
            L[i][column] = matrix[i][column]
    
    if(column == 2):
        for i in range(1, 4):
            L[i][column-2] = matrix[i][column-2]
        
        for i in range(2, 4):
            L[i][column-1] = matrix[i][column-1]

        
        for i in range(3, 4):
            L[i][column] = matrix[i][column]

    return L

def multiplyLU(matrixL, matrixU):

    A = np.zeros([4, 4])

    for i in range(0, 4):
        for j in range(0, 4):
            aux = 0
            aux = matrixL[i, :] * matrixU[:, j]

            el = 0
            for k in range(0, (len(aux)-1)):
                el += aux[k]
            
            A[i][j] = el

    printLUMatrix(A)