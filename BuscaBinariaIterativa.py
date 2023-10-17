def buscaBinariaIterativa(vetor, item, tamanho):
	meio = 0
	inicio = 0
	fim = tamanho - 1
	while(inicio <= fim):
		meio = (inicio + fim) // 2
		if(item == vetor[meio]):			
			return meio
		elif(item > vetor[meio]):
			inicio = meio + 1
		else:
			fim = meio - 1
	return -1

if __name__ == '__main__':
	nValoreslista = input('Informe valores em ordem crescente: ').split()
	converterIntList = [int(i) for i in nValoreslista]
	print(converterIntList)
	chave = int(input('Que elemento vc deseja encontrar na lista: '))
	pos = buscaBinariaIterativa(converterIntList, chave, len(converterIntList))
	if(pos != -1):
		print(f'A chave {chave} está presente na posição {pos} da lista.')
	else:
		print(f'A chave {chave} não se encontra na lista.')