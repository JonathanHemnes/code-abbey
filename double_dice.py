def getDiceValue(r):
    return (r % 6) + 1

iterations = int(input())

answers = []

for i in range(iterations):
    values = input().split()
    r1, r2 = [int(i) for i in values]
    answers.append(getDiceValue(r1) + getDiceValue(r2))

answers = [str(i) for i in answers]

print(' '.join(answers))