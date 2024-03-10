def maxSumIncreasingSubsequence(array):
    # O(n ^ 2) time / O(n) space
    result = [float("-inf"), []]

    maxSums = []
    maxArrays = []
    for i in range(len(array)):
        sumToMerge = 0
        arrayToMerge = []
        for j in range(len(maxArrays)):
            if maxSums[j] > sumToMerge and maxArrays[j][-1] < array[i]:
                sumToMerge = maxSums[j]
                arrayToMerge = maxArrays[j]

        currentSum = sumToMerge + array[i]
        currentArray = arrayToMerge + [array[i]]
        maxSums.append(currentSum)
        maxArrays.append(currentArray)

        if currentSum > result[0]:
            result = [currentSum, currentArray]

    return result


print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
