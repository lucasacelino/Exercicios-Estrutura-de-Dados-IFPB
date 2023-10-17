def fibonacci(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
while(n != 0):
    for fib in range(n+1):
        print(fibonacci(fib), end=' ')
    print()
    n = int(input())