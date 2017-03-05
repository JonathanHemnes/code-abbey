values = input().split()

values = [int(i) for i in values]

min = max = values[0]

for i in values:
    if(i > max):
        max = i
    if(i < min):
        min = i

print(str(max) + ' ' + str(min))