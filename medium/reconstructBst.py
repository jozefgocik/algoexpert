# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution 1
# def reconstructBst(preOrderTraversalValues):
#     # O(n^2) time / O(h) space
#     if len(preOrderTraversalValues) == 0:
#         return None
#
#     currentValue = preOrderTraversalValues[0]
#     rightIdx = len(preOrderTraversalValues)
#
#     for idx in range(1, len(preOrderTraversalValues)):
#         value = preOrderTraversalValues[idx]
#         if value >= currentValue:
#             rightIdx = idx
#             break
#
#     root = BST(currentValue)
#     root.left = reconstructBst(preOrderTraversalValues[1:rightIdx])
#     root.right = reconstructBst(preOrderTraversalValues[rightIdx:len(preOrderTraversalValues)])
#
#     return root

# Solution 2
class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBst(preOrderTraversalValues):
    # O(n) time / O(n) space
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)

    return BST(rootValue, leftSubtree, rightSubtree)

print(reconstructBst([10, 4, 2, 1, 5, 17, 19, 18]))