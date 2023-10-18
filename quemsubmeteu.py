dictDeNomesDaPessoa = {}
listaDeNomesDeArquivos = []
listaDeNomesDeArquivosOrdenada = [] 
while True:
    nomeArquivoCompleto = input("Digite o nome do arquivo: ")
    nomeDaPessoa = nomeArquivoCompleto.split("-")[0]
    if nomeDaPessoa == "FIM":
        break
    if dictDeNomesDaPessoa.get(nomeDaPessoa) == None:
        dictDeNomesDaPessoa.update({nomeDaPessoa: nomeDaPessoa})
    listaDeNomesDeArquivos.append(nomeArquivoCompleto)

for k, v in dictDeNomesDaPessoa.items():
    for nomeDeArquivo in listaDeNomesDeArquivos:
        if v in nomeDeArquivo:
            listaDeNomesDeArquivosOrdenada.append(nomeDeArquivo)
for nomeDeArquivo in listaDeNomesDeArquivosOrdenada:
    print(nomeDeArquivo)