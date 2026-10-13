def fibo(n):
    if n <= 0:
        return 1

    return n * fibo(n-1)

print(fibo(5))