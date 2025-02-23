drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 3, 11, 42, 5, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

