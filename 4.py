words = open('./4.txt', 'r').read().split('\n')
total = 0
for word in words:
    winning_numbers = list(filter(None, word.split(':')[1].split('|')[0].split(' ')))
    numbers = list(filter(None, word.split(':')[1].split('|')[1].split(' ')))
    wins = 0
    for a in numbers:
        if a in winning_numbers:
            if wins: wins *= 2
            else: wins = 1
    total += wins
print(total)