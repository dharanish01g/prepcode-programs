# password = input("Enter the password: ")
# if len(password) < 8:
#     print("Password is small")
# else:
#     print("Password stored sucessfully")

password = "Hello"
special_character = "$"

if special_character in password:
    print("True")
else:
    print("False")