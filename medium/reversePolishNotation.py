def reversePolishNotation(tokens):
    # O(n) time / O(n) space
    operators = ["+", "-", "*", "/"]
    stack = []

    for i in range(len(tokens)):
        if tokens[i] in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            result = reversePolishNotationHelper(num1, num2, tokens[i])
            stack.append(result)
        else:
            stack.append(int(tokens[i]))

    return stack.pop()

def reversePolishNotationHelper(num1, num2, operator):
    if operator == "+":
        return num2 + num1
    elif operator == "-":
        return num2 - num1
    elif operator == "*":
        return num2 * num1
    else:
        return int(num2 / num1)

print(reversePolishNotation(["50", "3", "17", "+", "2", "-", "/"]))
print(reversePolishNotation(["18", "4", "-", "7", "/"]))