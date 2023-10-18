dictNomes = {}
dados = input()
while(dados != 'FIM'):
    nome, numero = dados.split()
    dictNomes[nome] = numero
    dados = input()

buscaValorChave = input()
while(buscaValorChave != 'FIM'):
    print(dictNomes.get(buscaValorChave))
    buscaValorChave = input()