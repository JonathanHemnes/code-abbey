iterations = input()

def getMin(inputs):
    min = int(inputs[0])
    for i in inputs:
        if(int(i) < min):
            min = int(i)
    return min

answers = []

for i in range(int(iterations)):
    inputs = input().split()
    min = getMin(inputs)
    answers.append(str(min))

print(' '.join(answers))