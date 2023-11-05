# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        # Write your code here
        self.parents = {}

    def createSet(self, value):
        # O(1) time / O(1) space
        self.parents[value] = value

    def find(self, value):
        # O(n) time / O(1) space
        if value not in self.parents:
            return None

        currentParent = value
        while currentParent != self.parents[currentParent]:
            currentParent = self.parents[currentParent]

        return currentParent

    def union(self, valueOne, valueTwo):
        # O(n) time / O(1) space
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        self.parents[valueTwoRoot] = valueOneRoot
