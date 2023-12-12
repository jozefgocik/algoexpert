# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # O(1) time / O(1) space
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # O(1) time / O(1) space
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # O(1) time / O(1) space
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # O(1) time / O(1) space
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # O(p) time / O(1) space; p = until position, might be n
        if position == 1:
            self.setHead(nodeToInsert)
            return
        temp = self.head
        currentPosition = 1
        while temp is not None and currentPosition != position:
            temp = temp.next
            currentPosition += 1

        if temp is not None:
            self.insertBefore(temp, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # O(n) time / O(1) space
        temp = self.head
        while temp is not None:
            nodeToRemove = temp
            temp = temp.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # O(1) time / O(1) space
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        # O(n) time / O(1) space
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next

        return False
