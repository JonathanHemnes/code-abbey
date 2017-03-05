iterations = int(input())

def getSmallest(a, b):
    if (int(a) < int(b)):
        return a
    else:
        return b

answers = []

for i in range(iterations):
    a, b = input().split()
    min = getSmallest(a, b)
    answers.append(str(min))
print(' '.join(answers))

