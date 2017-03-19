alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

iterations, shift = input().split()
iterations =  int(iterations)
shift = int(shift)

for i in range(iterations):
    answer = []
    cipher = input()
    for c in cipher:
        if (c != '.' and c != ' '):
            charIndex = alphabet.index(c) - shift
            answer.append(str(alphabet[charIndex]))
        else:
            answer.append(c)
    print(''.join(answer))
    print(' ')