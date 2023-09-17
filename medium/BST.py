# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # O(Log(n)) time / O(1) space
        # Do not edit the return statement of this method.
        temp = self
        while temp is not None:
            if temp.value > value:
                if temp.left is None:
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    break
                temp = temp.right

        if temp.value > value:
            temp.left = BST(value)
        else:
            temp.right = BST(value)

        return self

    def contains(self, value):
        # O(Log(n)) time / O(1) space
        temp = self
        while temp is not None:
            if temp.value == value:
                return True
            elif temp.value > value:
                temp = temp.left
            else:
                temp = temp.right

        return False

    def remove(self, value, parentNode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while currentNode is not None:
            if currentNode.value > value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif currentNode.value < value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)

                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # Single node tree => Do nothing
                        pass

                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right

                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

                break

        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode.value


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

print(root.contains(1))

root.insert(12)
# self.assertTrue(root.right.left.left.value == 12)

root.remove(10)
# self.assertTrue(not root.contains(10))
# self.assertTrue(root.value == 12)
#
# self.assertTrue(root.contains(15))