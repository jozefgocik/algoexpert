# Solution 1
def minHeightBst(array):
    # O(nLog(n)) time / O(n) space
    return minHeightBstHelper(array, None, 0, len(array) - 1)

def minHeightBstHelper(array, tree, startIdx, endIdx):
    if endIdx < startIdx:
        return

    index = (startIdx + endIdx) // 2
    value = array[index]

    if tree is None:
        tree = BST(value)
    else:
        tree.insert(value)

    minHeightBstHelper(array, tree, startIdx, index - 1)
    minHeightBstHelper(array, tree, index + 1, endIdx)

    return tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


print(minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22]))
# print(minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36]))