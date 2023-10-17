def buscaSequencialRecursiva(lista, chave, ini = 0):
    if(ini >= len(lista)):
        return -1
    elif(chave == lista[ini]):
        return ini
    else:
        return buscaSequencialRecursiva(lista, chave, ini + 1)

if __name__ == '__main__':
    while True:
        busca = input('Deseja fazer uma busca na lista [S]im ou [N]ão: ')
        if(busca.upper() == 'S'):
            valoresListas = input('Adicione valores na lista: ').split()
            valoresInt = list(map(int, valoresListas))
            buscaChave = int(input('Que valor você deseja encontrar na lista: '))
            pos = buscaSequencialRecursiva(valoresInt, buscaChave)
            if(buscaChave == valoresInt[pos]):
                print(f'A chave {buscaChave} está presente na posição {pos} da lista')
            else:
                print(f'A chave {buscaChave} não foi encontrada lista.')
        elif(busca.upper() == 'N'):
            break
