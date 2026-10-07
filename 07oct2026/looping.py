number = int(input("Enter the Number: " ))
starting = 2
is_prime = True
while (starting < number):

    if number % starting == 0:
        is_prime = False
    starting += 1

print(is_prime)