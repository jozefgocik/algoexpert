# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def splitBinaryTree(tree):
    # O(n) time / O(h) space; h = height
    treeSum = getTreeSum(tree)
    canBeSplit = splitBinaryTreeHelper(tree, treeSum / 2)[1]
    if canBeSplit:
        return treeSum/2
    return 0

def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)


def splitBinaryTreeHelper(tree, desiredSum):
    # Write your code here.
    if tree is None:
        return (0, False)

    leftSum, leftCanBeSplit = splitBinaryTreeHelper(tree.left, desiredSum)
    rightSum, rightCanBeSplit = splitBinaryTreeHelper(tree.right, desiredSum)

    currerentSum = tree.value + leftSum + rightSum
    canBeSplit = leftCanBeSplit or rightCanBeSplit or currerentSum == desiredSum

    return (currerentSum, canBeSplit)