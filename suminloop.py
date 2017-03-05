iterations = input()
values = input().split()

def doSum(values):
    sum = 0
    for val in values:
        sum += int(val)
    return sum

total = doSum(values)

print(total)