text = input("Enter text: ")

frequencies = {}
for ch in text:
    if ch.isalpha():
        ch = ch.lower()
        if ch in frequencies:
            frequencies[ch] += 1
        else:
            frequencies[ch] = 1

for ch in sorted(frequencies):
    print(f"{ch}: {frequencies[ch]}")
