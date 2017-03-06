def approx_sq_root(value, a):
    r = 1
    for i in range(a):
        r = calculate_sq_root(value, r)
    return r

def calculate_sq_root(x,r):
    return (r + (x/r))/2

sequences = int(input())

answers = []

for i in range(sequences):
    value, i = input().split()
    answers.append(approx_sq_root(int(value), int(i)))

answers = [str(float(i)) for i in answers]

print(' '.join(answers))

