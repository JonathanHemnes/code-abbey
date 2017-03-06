def calculate_interest(s, p):
    return s * (1+ (p/100))

iterations = int(input())

answers = []

for i in range(iterations):
    s, r, p = input().split()
    s = int(s)
    r = int(r)
    p = int(p)

    iterations = 0
    while (s < r):
        s = calculate_interest(s, p)
        iterations = iterations + 1
    answers.append(str(iterations))
print(' '.join(answers))
    
    
