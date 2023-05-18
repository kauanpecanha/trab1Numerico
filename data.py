import numpy as np

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
