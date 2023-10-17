lista = ["Pedro", "Adnilton", "Alcimara", "José", "Allan", "Bastiao", "Ana Carolina", "Ana Júlia", "Severino", "Anderson", "André"]        
removeValor = int(input())
while len(lista) > 0:
    try:
        print(lista.pop(removeValor))
    except IndexError:
        print('ALÉM DO ÚLTIMO')
    removeValor = int(input())