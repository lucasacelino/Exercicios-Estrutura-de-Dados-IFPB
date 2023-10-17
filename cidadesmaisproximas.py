filiais = []
linha = input(': ')
while linha != 'fim':
    cidades = input('c: ')
    km = int(input('km: '))
    filiais.append((cidades, km))
    linha = input(': ')

if __name__== '__main__':
    filiais_proximas = sorted(filiais, key = lambda x: x[1])
    print(f'{filiais_proximas[0][0]}, {filiais_proximas[1][0]}')