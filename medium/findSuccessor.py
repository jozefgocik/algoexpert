# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Solution 1
# def findSuccessor(tree, node):
#     # O(n) time / O(n) space
#     array = findSuccessorHelper(tree, node, [])
#     for idx, currentNode in enumerate(array):
#         if currentNode == node:
#             if idx < len(array) - 1:
#                 return array[idx + 1]
#             return None
#
#
# def findSuccessorHelper(tree, node, array):
#     # Write your code here.
#     if tree is None:
#         return
#
#     findSuccessorHelper(tree.left, node, array)
#     array.append(tree)
#     findSuccessorHelper(tree.right, node, array)
#
#     return array

# Solution 2
def findSuccessor(tree, node):
    # O(h) time / O(1) space; h = height
    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)

def getLeftmostChild(node):
    temp = node
    while temp.left is not None:
        temp = temp.left

    return temp

def getRightmostParent(node):
    temp = node
    while temp.parent is not None and temp.parent.right == temp:
        temp = temp.parent

    return temp.parent