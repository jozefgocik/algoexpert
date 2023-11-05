# Solution 1
# def hasSingleCycle(array):
#     # O(n) time / O(n) space
#     indices = {}
#
#     currentIdx = 0
#     for i in range(0, len(array)):
#         if currentIdx not in indices:
#             indices[currentIdx] = 0
#         indices[currentIdx] += 1
#
#         if indices[currentIdx] > 1:
#             return False
#
#         currentIdx += array[currentIdx]
#         currentIdx = fixIndex(array, currentIdx)
#
#     currentIdx = fixIndex(array, currentIdx)
#     if currentIdx == 0:
#         return True
#
#     return False
#
# def fixIndex(array, currentIdx):
#     while currentIdx >= len(array):
#         currentIdx -= len(array)
#     while currentIdx < 0:
#         currentIdx += len(array)
#
#     return currentIdx

# Solution 2
def hasSingleCycle(array):
    # O(n) time / O(1) space
    currentIdx = 0

    for i in range(0, len(array)):
        if i > 0 and currentIdx == 0:
            return False

        currentIdx = getNextIdx(currentIdx, array)

    return currentIdx == 0

def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)

    while nextIdx < 0:
        nextIdx += len(array)

    return nextIdx

# print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
# print(hasSingleCycle([2, 2, -1]))
print(hasSingleCycle([2, 2, 2]))
print(hasSingleCycle([1, 1, 1, 1, 2]))
print(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]))
# print(hasSingleCycle([1, -1, 1, -1]))