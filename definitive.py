from data import matriz, matrizAumentada
from functions import printMatrix, determinePivot, swapPositions, zeroElementsBelow, createLMatrix, defineLElements, createUMatrix
L = createLMatrix(matrizAumentada)

# passo zero: imprimir a matriz inicial

print('\n\nA matriz original é:')
printMatrix(matrizAumentada)
print('\n')

# primeiro passo: definir o pivo da primeira coluna, e a linha pivotal

data = determinePivot(matriz, 0)
pivo = data[0]
linhaPivotal = data[1]

print(f'Pivo da primeira coluna: {pivo:.4f}, localizado na {linhaPivotal+1}° linha\n\n')

# segundo passo: permutar a linha da iteração pela linha pivotal

matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 0)

print(f'Depois de trocar a primeira linha pela {linhaPivotal+1}:')
printMatrix(matrizAumentada)

# terceiro passo: zerar os elementos abaixo do pivo usando os coeficientes

data = zeroElementsBelow(matrizAumentada, pivo, 0)
matrizAumentada = data[0]
m21 = data[1]
m31 = data[2]
m41 = data[3]

matrizAumentada[1][0] = m21
matrizAumentada[2][0] = m31
matrizAumentada[3][0] = m41

L = defineLElements(matrizAumentada, L, 0)

print(f'\n\nOs coeficientes: m21 = {m21:.4f}, m31 = {m31:.4f}, m41 = {m41:.4f}\n\n')
print(f'A matriz depois de zerar os elementos abaixo do primeiro pivo é:')
printMatrix(matrizAumentada)
print('\n\n')
print(f'A matriz L: \n{L}')
print('\n\n')

# quarto passo: definir o pivo da segunda coluna

data = determinePivot(matrizAumentada, 1)

pivo = data[0]
linhaPivotal = data[1]

print(f'Pivo da segunda coluna: {pivo:.4f}, localizado na {linhaPivotal+1}° linha')

# quinto passo: permutar a linha da iteração pela linha pivotal

matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 1)

print(f'Depois de trocar a segunda linha pela {linhaPivotal+1}:')
printMatrix(matrizAumentada)
print('\n\n')

# sexto passo: zerar os elementos abaixo do pivo

data = zeroElementsBelow(matrizAumentada, pivo, 1)
matrizAumentada = data[0]
m32 = data[1]
m42 = data[2]

matrizAumentada[2][1] = m32
matrizAumentada[3][1] = m42
L = defineLElements(matrizAumentada, L, 1)

print(f'\n\nOs coeficientes: m32 = {m32:.4f}, m42 = {m42:.4f}\n\n')

print(f'A matriz depois de zerar os elementos abaixo do segundo pivo é:')
printMatrix(matrizAumentada)
print('\n\n')
print(f'A matriz L: \n{L}')
print('\n\n')

# sétimo passo: determinar o pivo da terceira coluna

data = determinePivot(matrizAumentada, 2)

pivo = data[0]
linhaPivotal = data[1]

print(f'Pivo da terceira coluna: {pivo:.4f}, localizado na {linhaPivotal+1}° linha')

# oitavo passo: zerar os elementos abaixo do pivo

data = zeroElementsBelow(matrizAumentada, pivo, 2)
matrizAumentada = data[0]
m43 = data[1]

matrizAumentada[3][2] = m43
L = defineLElements(matrizAumentada, L, 2)

print(f'\n\nOs coeficientes: m43 = {m43:.4f}\n\n')

print(f'A matriz depois de zerar os elementos abaixo do terceiro pivo é:')
printMatrix(matrizAumentada)
print('\n\n')
print(f'A matriz L: \n{L}')
print('\n\n')

U = createUMatrix(matrizAumentada)
print(f'A matriz U: \n{U}')