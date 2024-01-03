def balancedBrackets(string):
    # O(n) time / O(n) space
    brackets = {"(": ")", "[": "]", "{": "}"}

    stack = []
    for i in range(0, len(string)):
        if string[i] in brackets.keys():
            stack.append(brackets[string[i]])
        elif string[i] in brackets.values():
            if len(stack) and string[i] == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(balancedBrackets("([])(){}(())()()"))
print(balancedBrackets("()[]{}{"))
