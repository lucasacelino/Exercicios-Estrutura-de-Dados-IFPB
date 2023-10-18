# exemplo de matriz 
"""
    matriz = [[1, 3, 2], [4, 5, 3]]. neste exemplo que eu fiz é mostrada uma matriz de 2 linhas e 3 colunas. Onde, a linha a 0 tem as colunas [1, 2, 3] e a linha 1 tem as colunas [4, 5, 3]
    
    também pode ser exemplificada dessa forma abaixo
    
    matriz = [
        0 = [1, 3, 2],
       1 = [4, 5, 3]
    ]
    
"""
matriz = [[1, 3, 2], [4, 5, 3]]

matrizExemplo = []
linhas = int(input("Informe a quantidade de linhas da matriz: "))
colunas = int(input("Informe a quantidade de coluna da matriz: "))

for linha in range(linhas):
    linhasMatriz = []
    print(f"linhaº {linha + 1}")
    for coluna in range(colunas):
        col = int(input(f"Informe um número para a coluna {coluna + 1}: "))
        linhasMatriz.append(col)
    matrizExemplo.append(linhasMatriz)

print(matrizExemplo)