
def getTemp(f):
    c = ((f + 40) / 1.8) - 40
    return round(c)

values = input().split()

values = values[1:]

values = [int(i) for i in values]

answers = [str(getTemp(i)) for i in values]

print(' '.join(answers))