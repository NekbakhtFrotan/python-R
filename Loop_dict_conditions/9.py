sentence = input("Enter a sentence: ")
words = sentence.lower().split()

frequencies = {}
for word in words:
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

for word, count in frequencies.items():
    print(f"{word}: {count}")


