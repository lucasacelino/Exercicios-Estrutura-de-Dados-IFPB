def BFSMenorCaminho(grafo, noOrigem, noDestino):
    verticesVisitados = []
    filaVertices = [[noOrigem]]
    while(len(filaVertices) > 0):
        caminho = filaVertices.pop(0)
        nos = caminho[-1]
        if nos not in verticesVisitados:
            vizinhos = grafo[nos]
            for verticesVizinhos in vizinhos:
                menorCaminho = list(caminho)
                menorCaminho.append(verticesVizinhos)
                filaVertices.append(menorCaminho)
                if verticesVizinhos == noDestino:
                    return menorCaminho
            verticesVisitados.append(nos)

def lerGrafo(Grafo):
    cidades = input()
    while(cidades != "FIM"):
        vertice, listaAdjacencias = cidades.split()
        listaAdjacencias = listaAdjacencias.split()
        if(vertice not in Grafo):
            Grafo[vertice] = []
        for no in listaAdjacencias:
            if(no not in Grafo[vertice]):
                Grafo[vertice].append(no)
            if(no not in Grafo):
                Grafo[no] = []
            if(vertice not in Grafo[no]):
                Grafo[no].append(vertice)
        cidades = input()
    return Grafo

grafo = {}
resultGrafo = lerGrafo(grafo)
percursoCidades = input()
while(percursoCidades != 'FIM'):
    percursoCidades = percursoCidades.split()
    resultPercurso = BFSMenorCaminho(resultGrafo, percursoCidades[0], percursoCidades[1])
    for rota in resultPercurso:
        print(rota, end=' ')
    print()
    percursoCidades = input()