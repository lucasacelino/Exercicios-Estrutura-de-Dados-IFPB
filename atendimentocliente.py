filaAtendimento_1 = []
while True:
    opcaoAtendimento = int(input())
    if(opcaoAtendimento == 1):
        nomeCliente, idadeCliente = input().split()
        filaAtendimento_1.append([nomeCliente, idadeCliente])
        filaAtendimento_2 = filaAtendimento_1[::-1]
        print(filaAtendimento_2)
    elif(opcaoAtendimento == 2):
        if(len(filaAtendimento_2) > 0):
            removerCliente = 0  
            print(filaAtendimento_2[removerCliente])
            filaAtendimento_2.pop(removerCliente)
        else:
            print('Vazia')
    elif(opcaoAtendimento == 3):
        ordemAtendimentoIdade = sorted(filaAtendimento_2, key = lambda x: x[1], reverse = True)
        for ordem in ordemAtendimentoIdade:
            print(ordem)
    elif(opcaoAtendimento == -1):
        break
    else:
        print('Opção inválida')