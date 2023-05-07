import numpy as np
import matplotlib.pyplot as plt

matriz = np.array([
    [2.94, 2.87, 2.33, 0],
    [1.48, 2.45, 2.89, -1.23],
    [6.31, 7.07, 2.79, 7.77],
    [8.27, -8.69, 8.79, -1.79],
    ])

matrizResultados = np.array([
    [2.63],
    [-4.38],
    [-7.83],
    [3.56]
    ])

matrizAumentada = np.concatenate((matriz, matrizResultados), axis=1)

# uma vez que a matriz quadrada é somente a matriz antes de ser aumentada, a pivotação parcial dependerá somente de seus dados,
# mas os resultados deverão ser surtidos na matriz aumentada.

matrizU = matriz # a matriz U é aquela que devemos utilizar para fazer a pivotação parcial

# encontrando o maior elemento da primeira coluna
pivo = 0

for i in range(0, 4):
    if(pivo < matrizU[i][0]):
        pivo = matrizU[i][0]
        linhaPivotal = i
    else:
        continue
# maior elemento da primeira coluna encontrado

# trocando as linhas
matrizAuxiliar = matrizAumentada[linhaPivotal].copy() # os dados da matriz auxiliar são todos uma cópia da linha pivotal da matriz aumentada
matrizAumentada[linhaPivotal] = matrizAumentada[0] # a primeira linha é levada para a antes linha pivotal
matrizAumentada[0] = matrizAuxiliar # e a primeira linha recebe os valores da linha pivotal

print(matrizAumentada)
# troca de linhas feita de forma correta