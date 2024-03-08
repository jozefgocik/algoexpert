# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sumBsts(tree):
    # O(n) time / O(h) space; h = height of BT
    return sumBstsHelper(tree).totalSum


def sumBstsHelper(tree):
    if tree is None:
        return TreeInfo(
            isBst=True,
            minValue=float("inf"),
            maxValue=float("-inf"),
            bstSum=0,
            bstSize=0,
            totalSum=0,
        )

    leftSubTree = sumBstsHelper(tree.left)
    rightSubTree = sumBstsHelper(tree.right)

    isBst = leftSubTree.isBst and rightSubTree.isBst and tree.value > leftSubTree.maxValue and tree.value <= rightSubTree.minValue

    minValue = min(tree.value, min(leftSubTree.minValue, rightSubTree.minValue))
    maxValue = max(tree.value, max(leftSubTree.maxValue, rightSubTree.maxValue))

    bstSum = 0
    bstSize = 0

    totalSum = leftSubTree.totalSum + rightSubTree.totalSum

    if isBst:
        bstSum = tree.value + leftSubTree.bstSum + rightSubTree.bstSum
        bstSize = 1 + leftSubTree.bstSize + rightSubTree.bstSize

        if bstSize >= 3:
            totalSum = bstSum

    return TreeInfo(
        isBst=isBst,
        minValue=minValue,
        maxValue=maxValue,
        bstSum=bstSum,
        bstSize=bstSize,
        totalSum=totalSum,
    )


class TreeInfo:
    def __init__(self, isBst, minValue, maxValue, bstSum, bstSize, totalSum):
        self.isBst = isBst
        self.minValue = minValue
        self.maxValue = maxValue
        self.bstSum = bstSum
        self.bstSize = bstSize
        self.totalSum = totalSum
