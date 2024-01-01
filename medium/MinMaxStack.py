# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        # O(1) time / O(1) space
        return self.stack[-1]

    def pop(self):
        # O(1) time / O(1) space
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        # O(1) time / O(1) space
        self.stack.append(number)
        if len(self.stack) == 1:
            self.minMaxStack.append([number, number])
        else:
            minValue = min(self.minMaxStack[-1][0], number)
            maxValue = max(self.minMaxStack[-1][1], number)
            self.minMaxStack.append([minValue, maxValue])

    def getMin(self):
        # O(1) time / O(1) space
        return self.minMaxStack[-1][0]

    def getMax(self):
        # O(1) time / O(1) space
        return self.minMaxStack[-1][1]
