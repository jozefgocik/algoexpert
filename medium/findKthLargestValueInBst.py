# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Solution 1
def findKthLargestValueInBst(tree, k):
    # O(h + k) time / O(h) space; h = tree height, k = input parameter
    return findKthLargestValueInBstHelper(tree, k, [])[k - 1]

def findKthLargestValueInBstHelper(tree, k, array):
    if tree is None or len(array) >= k:
        return

    findKthLargestValueInBstHelper(tree.right, k, array)
    array.append(tree.value)
    findKthLargestValueInBstHelper(tree.left, k, array)

    return array
