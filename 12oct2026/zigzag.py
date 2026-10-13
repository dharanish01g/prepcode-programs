num1 = int(input())
num2 = int(input())

for i in range(1, num1 + 1):
    for j in range (i, num2 + 1):
        if (i + j) % 4 == 0:
            print(i, j)