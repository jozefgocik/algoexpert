# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # O(n + e) time / O(n) space; v = number of nodes; e = numer of edges
        queue = [self]
        while queue:
            child = queue.pop(0)
            array.append(child.name)
            for i in child.children:
                queue.append(i)

        return array
