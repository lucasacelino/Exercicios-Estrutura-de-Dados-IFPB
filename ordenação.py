lista = []
linha = input()
while linha != 'fim':
    numeros = input().split()
    nInteiros = [int(i) for i in numeros]
    lista.append(nInteiros)
    linha = input()

listaOrdenada = [sorted(i) for i in lista]
for i in listaOrdenada:
    print(i)
print()

for lista in listaOrdenada:
    for i in range(len(lista)-1, -1, -1):
        print(lista[i], end =' ')
    print()