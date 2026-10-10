count = int(input("Enter the Number: "))
output = []
for i in range(1, count+1):
    if i % 3 == 0:
        if i % 5 == 0:
            output.append("fizzBuzz")
        else:
            output.append("Fizz")
    elif i % 5 == 0:
        output.append("Buzz")
    else:
        output.append(i)