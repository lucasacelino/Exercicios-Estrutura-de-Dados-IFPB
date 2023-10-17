valores = input().split()
x, n = float(valores[0]), int(valores[1])
for i in range(n+1):
    s = x ** i
    print(f'{s:.6f}', end= ' ')