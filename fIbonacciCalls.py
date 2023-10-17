contador = 0
def fib(n):
    global contador
    contador += 1  
    if(n == 0 or n == 1):
        return n
    else: 
        return fib(n-1) + fib(n-2)
    
n = int(input())
while(n != 39):
    print(f'fib({n}) = {fib(n)} calls = {contador-1}')
    n = int(input())
    contador = 0