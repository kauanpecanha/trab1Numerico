import numpy as np
import matplotlib.pyplot as plt

# função para impressão da matriz
def printMatrix(matrix):
    i = 0
    j = 0

    for i in range(0, 4):
        for j in range(0, 5):
            if(j == 4):
                print(f'{matrix[i][j]:.4f} ')
            else:
                print(f'{matrix[i][j]:.4f} ', end='')

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

        matrix[1, :] = matrix[1, :] + matrix[0, :] * m21
        matrix[2, :] = matrix[2, :] + matrix[0, :] * m31
        matrix[3, :] = matrix[3, :] + matrix[0, :] * m41

        return [matrix, m21, m31, m41]
    
    elif(column == 1):
        
        m32 = -((matrix[2][1])/pivot)
        m42 = -((matrix[3][1])/pivot)

        matrix[2, :] = matrix[2, :] + matrix[1, :] * m32
        matrix[3, :] = matrix[3, :] + matrix[1, :] * m42

        return [matrix, m32, m42]
    
    elif(column == 2):

        m43 = -((matrix[3][2])/pivot)

        matrix[3, :] = matrix[3, :] + matrix[2, :] * m43

        return [matrix, m43]
