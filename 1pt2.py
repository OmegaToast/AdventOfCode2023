words = open('./1.txt', 'r').read().split("\n")
numbers = ['one','two','three','four','five','six','seven','eight','nine']
total = 0
for word in words:
    while True:
        num = None
        lowest_index = 999
        for i,n in enumerate(numbers):
            if n in word:
                if word.index(n) < lowest_index:
                    num = i
                    lowest_index = word.index(n)
        if num == None: break
        else: word = word[:lowest_index+1] + str(num+1) + word[lowest_index+1:]
    first = None
    for letter in word:
        if letter.isnumeric():
            last = letter
            if not first:
                first = letter
    total += int(first+last)
print(total)