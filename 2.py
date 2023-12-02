words = open('./2.txt', 'r').read().split('\n')
total = 0
max_marbles = {'red':12,'green':13,'blue':14}
for word in words:
    game = '; '.join(word.split(': ')[1].split(', ')).split('; ')
    posible = True
    for pair in game:
        split = pair.split(' ')
        if max_marbles[split[1]] < int(split[0]):
            posible = False
    if posible: total += int(word.removeprefix('Game ').split(':')[0])
print(total)