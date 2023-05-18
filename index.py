import numpy as np
import matplotlib.pyplot as plt

from functions import printMatrix, swapPositions, determinePivot, zeroElementsBelow
from data import matriz, matrizResultados, matrizAumentada, matrizPermutacao


# determinação do pivo da primeira coluna
data = determinePivot(matrizAumentada, 0)
pivo = data[0]
linhaPivotal = data[1]

# trocando as linhas
matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 0)

# zerando os elementos abaixo do pivo e armazenando os coeficientes
data = zeroElementsBelow(matrizAumentada, pivo, 0)
matrizAumentada = data[0]
m21 = data[1]
m31 = data[2]
m41 = data[3]

# determinação do pivo da segunda coluna
data = determinePivot(matrizAumentada, 1)

pivo = data[0]
linhaPivotal = data[1]


# trocando as linhas
matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 1)


# zerando os elementos abaixo do pivo e armazenando os coeficientes
data = zeroElementsBelow(matrizAumentada, pivo, 1)
matrizAumentada = data[0]
m32 = data[1]
m42 = data[2]

# determinação do pivo da terceira coluna
data = determinePivot(matrizAumentada, 2)

pivo = data[0]
linhaPivotal = data[1]

# não haverá troca de linhas, pois a linha pivotal já está no lugar que deveria estar

data = zeroElementsBelow(matrizAumentada, pivo, 2)
matrizAumentada = data[0]
m43 = data[1]

printMatrix(matrizAumentada)

A = matrizAumentada