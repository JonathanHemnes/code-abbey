words = input().split()

wordset = {}

answers = set()

for w in words:
    try:
        wordset[w] = wordset[w] + 1
        answers.add(w)
    except KeyError:
        wordset[w] = 1
        
print(' '.join(sorted(answers)))