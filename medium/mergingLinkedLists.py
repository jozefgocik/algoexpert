# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Solution 1
# def mergingLinkedLists(linkedListOne, linkedListTwo):
#     # O(n * m) time / O(1) space
#     nodeOne = linkedListOne
#     while nodeOne is not None:
#         nodeTwo = linkedListTwo
#         while nodeTwo is not None:
#             if nodeOne.value == nodeTwo.value:
#                 return nodeOne
#             nodeTwo = nodeTwo.next
#         nodeOne = nodeOne.next
#
#     return None

# Solution 2
def mergingLinkedLists(linkedListOne, linkedListTwo):
    # O(n + m) time / O(1) space
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None:
        if nodeOne.value == nodeTwo.value:
            return nodeOne

        nodeOne = nodeOne.next
        nodeTwo = nodeTwo.next
        if nodeOne is None and nodeTwo is not None:
            nodeOne = linkedListTwo
        if nodeTwo is None and nodeOne is not None:
            nodeTwo = linkedListOne

    return None