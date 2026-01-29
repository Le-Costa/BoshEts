import numpy as np

# Sudoku é valido se depois de ordenar corresponder a [1,2...,9]-> np.arange(1,10)
# np.array_equal: retorna true se duas matrizes forem iguais

tabuleiro = np.random.randint(0, 10, 81).reshape(9, 9)
print(tabuleiro)
ver = True
for linha in tabuleiro:
    # np.sort-> ordena os numeros da linha;np.arange-> cria um vetor de 1 a 9 e equal compara eles
    if not np.array_equal(np.sort(linha), np.arange(1, 10)):
        ver = False

for c in tabuleiro.T:  # .T transpoe a matriz linhas viram colunas e colunas viram linhas
    if not np.array_equal(np.sort(c), np.arange(1, 10)):
        ver = False

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        bloco = tabuleiro[i:i+3, j:+3].flatten()

        if not np.array_equal(np.sort(bloco), np.arange(1, 10)):
            ver = False
