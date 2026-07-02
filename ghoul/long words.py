def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest, len(longest)

words = ["apple", "banana", "cherry", "kiwi", "mango", "UFHFJHGKJGKJGKJHIU"]

word, length = longest_word(words)

print("Longest_word:", word)
print("Length:", length)

text = "apple,banana,mango,orange,grapes"
entries = text.split(",")
print (entries)