from data import matriz, matrizAumentada, matrizPermutacao
from functions import printMatrix, determinePivot, swapPositions, zeroElementsBelow, createLMatrix, defineLElements, createUMatrix, printLUMatrix, multiplyLU



print('-'*100 + '\nPrimeiro passo: Impressão da Matriz em estado inicial')



L = createLMatrix(matrizAumentada)
print('\n\nA matriz original é:\n')
printMatrix(matrizAumentada)
print('\n\n')



print('-'*100 + '\nSegundo passo: Definição do pivo da primeira coluna e da linha pivotal')



data = determinePivot(matriz, 0)
pivo = data[0]
linhaPivotal = data[1]
print(f'\n\nPivo da primeira coluna: {pivo:.2f}, localizado na {linhaPivotal+1}° linha\n\n')



print('-'*100 + '\nTerceiro passo: Permutação da primeira linha pela linha pivotal')



matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 0)
matrizPermutacao = swapPositions(matrizPermutacao, linhaPivotal, 0)
print(f'\n\nDepois de trocar a primeira linha pela {linhaPivotal+1}:')
printMatrix(matrizAumentada)
print('\n\n')



print('-'*100 + '\nQuarto passo: Efetuação das operações para zerar os elementos abaixo do pivo')



data = zeroElementsBelow(matrizAumentada, pivo, 0)
matrizAumentada = data[0]
m21 = data[1]
m31 = data[2]
m41 = data[3]
print('\n\nMatriz com os elementos abaixo do primeiro pivo zerados:')
printMatrix(matrizAumentada)
matrizAumentada[1][0] = m21
matrizAumentada[2][0] = m31
matrizAumentada[3][0] = m41
print('\n\nSubstituindo os zeros pelos coeficientes:')
printMatrix(matrizAumentada)
L = defineLElements(matrizAumentada, L, 0)
U = createUMatrix(matrizAumentada)
print(f'\n\nOs coeficientes: m21 = {m21:.2f}, m31 = {m31:.2f}, m41 = {m41:.2f}\n\n')
print('A matriz L:')
printLUMatrix(L)
print('\n\n')
print('A matriz U:')
printLUMatrix(U)
print('\n\n')



print('-'*100 + '\nQuinto passo: Definição do pivo da segunda coluna')



data = determinePivot(matrizAumentada, 1)
pivo = data[0]
linhaPivotal = data[1]
print(f'\n\nPivo da segunda coluna: {pivo:.2f}, localizado na {linhaPivotal+1}° linha\n\n')



print('-'*100 + '\nSexto passo: Permutação da segunda linha pela linha pivotal')



matrizAumentada = swapPositions(matrizAumentada, linhaPivotal, 1)
matrizPermutacao = swapPositions(matrizPermutacao, linhaPivotal, 1)
print(f'\n\nDepois de trocar a segunda linha pela {linhaPivotal+1}:')
printMatrix(matrizAumentada)
print('\n\n')



print('-'*100 + '\nSétimo passo: Efetuação das operações para zerar os elementos abaixo do pivo')



data = zeroElementsBelow(matrizAumentada, pivo, 1)
matrizAumentada = data[0]
m32 = data[1]
m42 = data[2]
print('\n\nMatriz com os elementos abaixo do segundo pivo zerados:')
printMatrix(matrizAumentada)
matrizAumentada[2][1] = m32
matrizAumentada[3][1] = m42
print('\n\nSubstituindo os zeros pelos coeficientes:')
printMatrix(matrizAumentada)
L = defineLElements(matrizAumentada, L, 1)
U = createUMatrix(matrizAumentada)
print(f'\n\nOs coeficientes: m32 = {m32:.2f}, m42 = {m42:.2f}\n\n')
print('A matriz L:')
printLUMatrix(L)
print('\n\n')
print('A matriz U:')
printLUMatrix(U)



print('-'*100 + '\nOitavo passo: determinação do pivo da terceira coluna')



data = determinePivot(matrizAumentada, 2)
pivo = data[0]
linhaPivotal = data[1]
print(f'\n\nPivo da terceira coluna: {pivo:.2f}, localizado na {linhaPivotal+1}° linha\n\n')



print('-'*100 + '\nNono passo: Efetuação das operações para zerar os elementos abaixo do pivo')



data = zeroElementsBelow(matrizAumentada, pivo, 2)
matrizAumentada = data[0]
m43 = data[1]
print('\n\nMatriz com os elementos abaixo do segundo pivo zerados:')
printMatrix(matrizAumentada)
matrizAumentada[3][2] = m43
print('\n\nSubstituindo os zeros pelos coeficientes:')
printMatrix(matrizAumentada)
L = defineLElements(matrizAumentada, L, 2)
U = createUMatrix(matrizAumentada)
print(f'\n\nOs coeficientes: m43 = {m43:.2f}\n\n')



print('-'*100 + '\nDécimo passo: Impressão da Matriz Final, da Matriz L, e Matriz U')



print(f'\n\nMatriz final: \n')
printMatrix(matrizAumentada)
print('\n\n')
print('A matriz L: \n')
printLUMatrix(L)
print('\n\n')
print('A matriz U: \n')
printLUMatrix(U)
print('\n\n')
print('Operação L * U: \n')
multiplyLU(L, U)
print(f'\n\nNúmero de Passos: {10}\n\n')
print('\n\nMatriz de permutações: \n\n')
printLUMatrix(matrizPermutacao)