# Solution 1
# def maxSumIncreasingSubsequence(array):
#     # O(n ^ 2) time / O(n ^ 2) space
#     result = [float("-inf"), []]
#
#     maxSums = []
#     maxArrays = []
#     for i in range(len(array)):
#         sumToMerge = 0
#         arrayToMerge = []
#         for j in range(len(maxArrays)):
#             if maxSums[j] > sumToMerge and maxArrays[j][-1] < array[i]:
#                 sumToMerge = maxSums[j]
#                 arrayToMerge = maxArrays[j]
#
#         currentSum = sumToMerge + array[i]
#         currentArray = arrayToMerge + [array[i]]
#         maxSums.append(currentSum)
#         maxArrays.append(currentArray)
#
#         if currentSum > result[0]:
#             result = [currentSum, currentArray]
#
#     return result

# Solution 2
def maxSumIncreasingSubsequence(array):
    # O(n ^ 2) time / O(n) space
    sequences = [None for _ in array]
    sums = array[:]
    maxSumIdx = 0

    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]

    return sequence[::-1]


print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
