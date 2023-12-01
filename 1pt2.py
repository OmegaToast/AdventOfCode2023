##
# Dosn't work :(
##
file = open('./1.txt', 'r')
words = file.read().split("\n")

numbers = ['one','two','three','four','five','six','seven','eight','nine']

total = 0
for word in words:
    while True:
        num = None
        lowest_index = 999
        for i,n in enumerate(numbers):
            try:
                if word.index(n) < lowest_index:
                    num = i
                    lowest_index = word.index(n)
            except ValueError:
                pass
        if num == None:
            break
        else:
            print("  ",numbers[num])
            word = str(num+1).join(word.split(numbers[num]))
    print(word)
    first = None
    last = None
    for letter in word:
        if letter.isnumeric():
            last = letter
            if not first:
                first = letter
    total += int(first+last)
print(total)