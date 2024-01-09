def sortStack(stack):
    # O(n ^ 2) time / O(n) space
    if not stack:
        return stack

    currentNum = stack.pop()
    sortStack(stack)
    sortStackHelper(stack, currentNum)

    return stack

def sortStackHelper(stack, currentNum):
    if len(stack) == 0:
        stack.append(currentNum)
    elif currentNum > stack[-1]:
        stack.append(currentNum)
    else:
        num = stack.pop()
        sortStackHelper(stack, currentNum)
        stack.append(num)

print(sortStack([-5, 2, -2, 4, 3, 1]))