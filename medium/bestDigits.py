def bestDigits(number, numDigits):
    # O(n) time / O(n) space
    stack = []

    for i in range(0, len(number)):
        currentNumber = number[i]
        while numDigits > 0 and len(stack) > 0 and currentNumber > stack[len(stack) - 1]:
            stack.pop()
            numDigits -= 1
        stack.append(currentNumber)

    return "".join(stack[0:len(number) - numDigits])

print(bestDigits("462839",2))

