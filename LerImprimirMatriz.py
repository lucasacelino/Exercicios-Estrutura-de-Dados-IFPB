matriz = []
n, m = map(int, input().split())
while(n != 0 or m != 0):
    for i in range(n):
        matriz.append(list(map(int, input().split())))
          
    for linha in range(n):
        for coluna in range(m):
            print(matriz[linha][coluna], end=" ")
        print()
    
    print()
    matriz.clear()
    n, m = map(int, input().split())