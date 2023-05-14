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


# inicialização da matriz original
matriz = np.array([
    [2.94, 2.87, 2.33, 0],
    [1.48, 2.45, 2.89, -1.23],
    [6.31, 7.07, 2.79, 7.77],
    [8.27, -8.69, 8.79, -1.79],
    ])

# inicialização da matriz de resultados
matrizResultados = np.array([
    [2.63],
    [-4.38],
    [-7.83],
    [3.56]
    ])

# concatenação da matriz original com sua matriz de resultados
matrizAumentada = np.concatenate((matriz, matrizResultados), axis=1)


matrizPermutacao = np.array([1, 2, 3, 4])

# determinação do pivo da primeira coluna
pivo = 0
for i in range(0, 4):
    if(pivo < matrizAumentada[i][0]):
        pivo = matrizAumentada[i][0]
        linhaPivotal = i
    else:
        continue


# trocando as linhas
matrizAuxiliar = matrizAumentada[linhaPivotal].copy() # os dados da matriz auxiliar são todos uma cópia da linha pivotal da matriz aumentada
matrizAumentada[linhaPivotal] = matrizAumentada[0] # a primeira linha é levada para a antes linha pivotal
matrizAumentada[0] = matrizAuxiliar # e a primeira linha recebe os valores da linha pivotal


# determinação dos coeficientes
m21 = -((matrizAumentada[1][0])/pivo)
m31 = -((matrizAumentada[2][0])/pivo)
m41 = -((matrizAumentada[3][0])/pivo)


# zerando as linhas da primeira coluna
matrizAumentada[1, :] = matrizAumentada[1, :] + matrizAumentada[0, :] * m21
matrizAumentada[2, :] = matrizAumentada[2, :] + matrizAumentada[0, :] * m31
matrizAumentada[3, :] = matrizAumentada[3, :] + matrizAumentada[0, :] * m41


# determinação do pivo da segunda coluna
pivo = 0 # inicialização
for i in range(1, 4):
    if(pivo < matrizAumentada[i][1]):
        pivo = matrizAumentada[i][1]
        linhaPivotal = i
    else:
        continue


# trocando as linhas
matrizAuxiliar = matrizAumentada[linhaPivotal].copy() 
matrizAumentada[linhaPivotal] = matrizAumentada[1] 
matrizAumentada[1] = matrizAuxiliar 


# determinação dos coeficientes
m32 = -((matrizAumentada[2][1])/pivo)
m42 = -((matrizAumentada[3][1])/pivo)


# zerando as linhas da segunda coluna
matrizAumentada[2, :] = matrizAumentada[2, :] + matrizAumentada[1, :] * m32
matrizAumentada[3, :] = matrizAumentada[3, :] + matrizAumentada[1, :] * m42


# determinação do pivo da terceira coluna
pivo = 0 # inicialização
for i in range(2, 4):
    if(pivo < matrizAumentada[i][2]):
        pivo = matrizAumentada[i][2]
        linhaPivotal = i
    else:
        continue


# não haverá troca de linhas, pois a linha pivotal já está no lugar que deveria estar


# determinação dos coeficientes
m43 = -((matrizAumentada[3][2])/pivo)


# zerando as linhas da terceira coluna
matrizAumentada[3, :] = matrizAumentada[3, :] + matrizAumentada[2, :] * m43

printMatrix(matrizAumentada)

# nota: todos os elementos abaixo da diagonal principal foram zerados com sucesso: conferir posteriormente se os coeficientes de cada linha e coluna estão corretos