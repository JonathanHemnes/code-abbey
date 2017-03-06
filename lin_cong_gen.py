def getNext(a, c, m, x):
    return (a * x + c) % m

iterations = int(input())

answers = []

for i in range(iterations):
    a, c, m, x, n = input().split()
    a = int(a)
    c = int(c)
    x = int(x)
    m = int(m)
    n = int(n)

    for j in range(n):
        x = getNext(a, c, m, x)
        
    answers.append(str(x))
print(' '.join(answers))