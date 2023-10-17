figurinhasJoao = []
adicionarFigurinhasJoao = input()
while(adicionarFigurinhasJoao != 'FIM'):
    figurinhasJoao.append(adicionarFigurinhasJoao)
    adicionarFigurinhasJoao = input()

figurinhasPedro = []
adicionarFigurinhasPedro = input()
while(adicionarFigurinhasPedro != 'FIM'):
    figurinhasPedro.append(figurinhasJoao.count(adicionarFigurinhasPedro))
    adicionarFigurinhasPedro = input()

for i in figurinhasPedro:
    print(i)