matriz = []
addNumMatriz = input()
while(addNumMatriz != "FIM"):
    vetor = list(map(int, input().split()))
    
    linhasNumerosMatriz = input()
    while(linhasNumerosMatriz != " "):
        numeros = linhasNumerosMatriz.split()
        numerosCasting = [int(i) for i in numeros]
        matriz.append(numerosCasting)
        linhasNumerosMatriz = input()
    
    
