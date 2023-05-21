import numpy as np
import matplotlib.pyplot as plt

from functions import printMatrix, swapPositions, determinePivot, zeroElementsBelow
from data import matriz, matrizResultados, matrizAumentada, matrizPermutacao

print('\n\nA matriz original é:')
printMatrix(matrizAumentada)
print('\n')

# determinação do pivo da primeira coluna
data = determinePivot(matrizAumentada, 0)
pivo = data[0]
linhaPivotal = data[1]

print(f'Pivo da primeira coluna: {pivo:.4f}, localizado na {linhaPivotal+1}° linha\n\n')

# trocando as linhas
matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 0)

print(f'Depois de trocar a primeira linha pela {linhaPivotal+1}:')
printMatrix(matrizAumentada)

# zerando os elementos abaixo do pivo e armazenando os coeficientes
data = zeroElementsBelow(matrizAumentada, pivo, 0)
matrizAumentada = data[0]
m21 = data[1]
m31 = data[2]
m41 = data[3]

print(f'\n\nOs coeficientes: m21 = {m21:.4f}, m31 = {m31:.4f}, m41 = {m41:.4f}\n\n')
print(f'A matriz depois de zerar os elementos abaixo do primeiro pivo é:')
printMatrix(matrizAumentada)
print('\n\n')

# determinação do pivo da segunda coluna
data = determinePivot(matrizAumentada, 1)

pivo = data[0]
linhaPivotal = data[1]

print(f'Pivo da segunda coluna: {pivo:.4f}, localizado na {linhaPivotal+1}° linha')

# trocando as linhas
matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 1)

print(f'Depois de trocar a segunda linha pela {linhaPivotal+1}:')
printMatrix(matrizAumentada)

# zerando os elementos abaixo do pivo e armazenando os coeficientes
data = zeroElementsBelow(matrizAumentada, pivo, 1)
matrizAumentada = data[0]
m32 = data[1]
m42 = data[2]

print(f'\n\nOs coeficientes: m32 = {m32:.4f}, m42 = {m42:.4f}\n\n')

print(f'A matriz depois de zerar os elementos abaixo do segundo pivo é:')
printMatrix(matrizAumentada)
print('\n\n')


# determinação do pivo da terceira coluna
data = determinePivot(matrizAumentada, 2)

pivo = data[0]
linhaPivotal = data[1]

print(f'Pivo da terceira coluna: {pivo:.4f}, localizado na {linhaPivotal+1}° linha')

# não haverá troca de linhas, pois a linha pivotal já está no lugar que deveria estar

data = zeroElementsBelow(matrizAumentada, pivo, 2)
matrizAumentada = data[0]
m43 = data[1]

print(f'\n\nOs coeficientes: m43 = {m43:.4f}\n\n')

print(f'A matriz depois de zerar os elementos abaixo do terceiro pivo é:')
printMatrix(matrizAumentada)
print('\n\n')

A = matrizAumentada