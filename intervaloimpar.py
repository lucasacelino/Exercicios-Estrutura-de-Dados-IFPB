numerosImpares = input().split()
impar1 = int(numerosImpares[0])
impar2 = int(numerosImpares[1])
for intervalo in range(impar1, impar2+1):
    if(intervalo % 2 == 1):
        print(intervalo, end = " ")