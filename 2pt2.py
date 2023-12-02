words = open('./2.txt', 'r').read().split('\n')
total = 0
for word in words:
    max_marbles = {'red':0,'green':0,'blue':0}
    game = '; '.join(word.split(': ')[1].split(', ')).split('; ')
    for pair in game:
        split = pair.split(' ')
        max_marbles[split[1]] = max(max_marbles[split[1]], int(split[0]))
    power = 1
    for i in max_marbles.values(): power *= i
    total += power
print(total)