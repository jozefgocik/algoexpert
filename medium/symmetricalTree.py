# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution 1
# def symmetricalTree(tree):
#     # O(n) time / O(n) space
#     return symmetricalTreeHelper(tree, [])
#
# def symmetricalTreeHelper(tree, array):
#     if tree is None:
#         return
#
#     symmetricalTreeHelper(tree.left, array)
#     array.append(tree.value)
#     symmetricalTreeHelper(tree.right, array)
#
#     return array == array[::-1]

# Solution 2
def symmetricalTree(tree):
    # O(n) time / O(h) space; h = height
    return symmetricalTreeHelper(tree.left, tree.right)

def symmetricalTreeHelper(left, right):
    if left is not None and right is not None and left.value == right.value:
        return symmetricalTreeHelper(left.left, right.right) and symmetricalTreeHelper(left.right, right.left)

    return left == right