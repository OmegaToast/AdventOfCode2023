words = open('./1.txt', 'r').read().split("\n")
total = 0
for word in words:
    first = None
    for letter in word:
        if letter.isnumeric():
            last = letter
            if not first:
                first = letter
    total += int(first+last)
print(total)