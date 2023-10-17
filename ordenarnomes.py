lista = []
linha = input()
while(linha != 'FIM'):
    lista.append(linha)
    linha = input()
lista.sort()
for i in range(len(lista)):
    for j in range(i+1):
        print(lista[j])
    print('**FIM**')