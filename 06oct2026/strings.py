sentence = input("Enter the Sentence")
print(sentence)

updated_sen = ""

for i in sentence:
    if i == " ":
        updated_sen = updated_sen + "-"
    else:
        updated_sen = updated_sen + i

print(updated_sen)
