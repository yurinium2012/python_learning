sentence = input("Enter a sentence: ")

count = 0
for char in sentence:
    if char in "AEIOU":
        count += 1
print("Total vowels:", count)