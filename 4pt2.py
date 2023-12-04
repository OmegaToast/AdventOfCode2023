words = open('./4.txt', 'r').read().split('\n')
cards_won = [1 for a in range(len(words))]
for w, word in enumerate(words):
    winning_numbers = list(filter(None, word.split(':')[1].split('|')[0].split(' ')))
    numbers = list(filter(None, word.split(':')[1].split('|')[1].split(' ')))
    wins = 0
    for a in numbers:
        if a in winning_numbers: wins += 1
    for a in range(wins):
        cards_won[w+a+1] += cards_won[w]
print(sum(cards_won))