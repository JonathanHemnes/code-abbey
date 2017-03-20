opening = '([{<'
closing = ')}]>'

iterations = int(input())

def isOpening(c):
    return opening.find(c) != -1

def isClosing(c):
    return closing.find(c) != -1

def isLastCharMatched(stack, c):
    lastChar = stack[len(stack)-1]
    if (c == ')'):
        return lastChar == '('
    elif (c == '}'):
        return lastChar == '{'
    elif (c == ']'):
        return lastChar == '['
    elif (c == '>'):
        return lastChar == '<'

def isWellFormed(chars):
    stack = []
    for c in chars:
        if(isOpening(c)):
            stack.append(c)

        elif (isClosing(c)):
            
            if(len(stack) > 0 and isLastCharMatched(stack, c)):
                stack.pop()
            
            else:
                return 0
    return 1 if len(stack) == 0 else 0

answers = []

for i in range(iterations):
    chars = list(input())
    answers.append(str(isWellFormed(chars)))

print(' '.join(answers))
