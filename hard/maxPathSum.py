def maxPathSum(tree):
    # O(n) time / O(log(n)) space
    return maxPathSumHelper(tree).totalSum


def maxPathSumHelper(tree):
    if tree is None:
        return TreeInfo(
            branchSum=0,
            triangleSum=0,
            totalSum=float("-inf")
        )

    leftSubtree = maxPathSumHelper(tree.left)
    rightSubtree = maxPathSumHelper(tree.right)

    branchSum = tree.value + max(leftSubtree.branchSum, rightSubtree.branchSum)
    triangleSum = tree.value + leftSubtree.branchSum + rightSubtree.branchSum
    totalSum = max(branchSum, triangleSum, leftSubtree.totalSum, rightSubtree.totalSum)

    return TreeInfo(
        branchSum,
        triangleSum,
        totalSum,
    )


class TreeInfo:
    def __init__(self, branchSum, triangleSum, totalSum):
        self.branchSum = branchSum
        self.triangleSum = triangleSum
        self.totalSum = totalSum
