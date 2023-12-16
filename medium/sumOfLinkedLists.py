# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # O(max(n, m)) time / O(max(n, m)) space; n = len(linkedListOne), m = len(linkedListTwo)
    linkedListHeadPointer = LinkedList(0)
    currentNode = linkedListHeadPointer

    carry = 0
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0

        sum = valueOne + valueTwo + carry
        newValue = sum % 10

        currentNode.next = LinkedList(newValue)
        currentNode = currentNode.next

        carry = sum // 10

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None


    return linkedListHeadPointer.next