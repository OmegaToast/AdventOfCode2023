words = open('./3.txt', 'r').read().split('\n')
total = 0
big_list = []
for x, s in enumerate(words):
    big_list.append([])
    for v in s:
        big_list[x].append(v)
for x, s in enumerate(big_list):
    number = 0
    valid = False
    for y, v in enumerate(s):
        if v.isnumeric():
            number *= 10
            number += int(v)
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    try:
                        symbol = big_list[x+a][y+b]
                        if (not symbol.isnumeric()) and (symbol != '.'):
                            valid = True
                    except:
                        pass
        elif valid:
            total += number
            number = 0
            valid = False
print(total)