iterations = input()
answers = []
for i in range(int(iterations)):
    a,b = input().split()
    sum = int(a) + int(b)
    answers.append(str(sum))
print(' '.join(answers))