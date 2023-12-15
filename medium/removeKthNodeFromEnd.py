# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Solution 1
# def removeKthNodeFromEnd(head, k):
#     # O(n * (l - k)) time / O(1) space; l = length of the LinkedList
#     length = 0
#     node = head
#     while node is not None:
#         length += 1
#         node = node.next
#
#     nodeBefore = None
#     node = head
#     for i in range(0, length - k):
#         nodeBefore = node
#         node = node.next
#
#     if node == head:
#         head.value = node.next.value
#         head.next = node.next.next
#     else:
#         nodeBefore.next = node.next

# Solution 2
# def removeKthNodeFromEnd(head, k):
#     # O(n) time / O(1) space
#     nodeBefore = None
#     first = head
#     second = head
#
#     for i in range(0, k):
#         second = second.next
#     while second is not None:
#         nodeBefore = first
#         first = first.next
#         second = second.next
#
#     if first == head:
#         head.value = first.next.value
#         head.next = first.next.next
#     else:
#         nodeBefore.next = first.next

# Solution 3
def removeKthNodeFromEnd(head, k):
    # O(n) time / O(1) space
    first = head
    second = head
    for i in range(0, k):
        second = second.next
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
