matriz = []
addMatrizEscalar = input()
while(addMatrizEscalar != "FIM"):
    numeroEscalar = int(input())
    
    linhaNumerosMatriz = input()
    while(linhaNumerosMatriz != " "):
        linhasNumeros = linhaNumerosMatriz.split()
        numerosCastingInt = [int(i) for i in linhasNumeros]
        matriz.append(numerosCastingInt)
        linhaNumerosMatriz = input()
        
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna] * numeroEscalar, end=" ")
        print()
    
    print()
    matriz.clear()
    addMatrizEscalar = input()