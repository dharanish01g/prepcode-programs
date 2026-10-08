words = "Hello World! 123"
vowels_count = 0

vowels = ["a", "e", "i", "o", "u"]

for i in vowels:
    vowels_count = vowels_count + words.count(i)

print(vowels_count)