# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution 1
def mergeBinaryTrees(tree1, tree2):
    # O(n) time / O(h) space; h = height
    return mergeBinaryTreesHelper(tree1, tree2)

def mergeBinaryTreesHelper(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value

    tree1.left = mergeBinaryTreesHelper(tree1.left, tree2.left)
    tree1.right = mergeBinaryTreesHelper(tree1.right, tree2.right)

    return tree1