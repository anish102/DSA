score = [5, 4, 3, 6, 2, 1]
pair = {}

sor = sorted(score, reverse=True)

for i in range(len(sor)):
    if i == 0:
        pair[sor[i]] = "Gold Medal"
    elif i == 1:
        pair[sor[i]] = "Silver Medal"
    elif i == 2:
        pair[sor[i]] = "Bronze Medal"
    else:
        pair[sor[i]] = str(i + 1)

print([pair[i] for i in score])
