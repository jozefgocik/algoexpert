# Solution 1
# def sameBsts(arrayOne, arrayTwo):
#     # O(n ^ 2) time / O(n ^ 2) space
#     if not arrayOne and not arrayTwo:
#         return True
#     if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
#         return False
#     else:
#         root = arrayOne[0]
#         arrayOneLeftSubtree = [num for num in arrayOne[1:len(arrayOne)] if num < root]
#         arrayOneRightSubtree = [num for num in arrayOne[1:len(arrayOne)] if num >= root]
#         arrayTwoLeftSubtree = [num for num in arrayTwo[1:len(arrayTwo)] if num < root]
#         arrayTwoRightSubtree = [num for num in arrayTwo[1:len(arrayTwo)] if num >= root]
#
#         return sameBsts(arrayOneLeftSubtree, arrayTwoLeftSubtree) and sameBsts(arrayOneRightSubtree, arrayTwoRightSubtree)

# Solution 2
def sameBsts(arrayOne, arrayTwo):
    # O(n ^ 2) time / O(d) space; d = depth of BST
    return areSameBSTs(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def areSameBSTs(arrayOne, arrayTwo, rootIndexOne, rootIndexTwo, minVal, maxVal):
    if rootIndexOne == -1 or rootIndexTwo == -1:
        return rootIndexOne == rootIndexTwo
    if arrayOne[rootIndexOne] != arrayTwo[rootIndexTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIndexOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIndexTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIndexOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIndexTwo, maxVal)

    currentValue = arrayOne[rootIndexOne]
    leftAreSame = areSameBSTs(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBSTs(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame

def getIdxOfFirstSmaller(array, startIdx, minVal):
    for i in range(startIdx + 1, len(array)):
        if array[i] < array[startIdx] and array[i] >= minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startIdx, maxVal):
    for i in range(startIdx + 1, len(array)):
        if array[i] >= array[startIdx] and array[i] < maxVal:
            return i
    return -1


print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))