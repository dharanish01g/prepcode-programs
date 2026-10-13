def add(n):
    if n <= 0:
        return 0
    
    if n % 2 == 0:
        return n + add(n-1)
    else:
        return add(n-1)
print(add(10))