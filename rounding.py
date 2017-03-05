iterations = int(input())

answers = []

for i in range(iterations):
    a,b = input().split()
    a = int(a)
    b = int(b)
    answers.append(round(a / b))

answers = [str(i) for i in answers]

print(' '.join(answers))