cadastroAlunosBOCA = input().split(',')
buscaAlunosBOCA = input()
while(buscaAlunosBOCA != 'FIM'):
    if buscaAlunosBOCA in cadastroAlunosBOCA:
        print(f'{buscaAlunosBOCA} PRESENTE')
    else:
        print(f'{buscaAlunosBOCA} AUSENTE')
    buscaAlunosBOCA = input()