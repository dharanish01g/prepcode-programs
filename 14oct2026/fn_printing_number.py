def printer(n, count=1):
    if count > n:
        return
    print(count)
    printer(n, count+1)

printer(5)