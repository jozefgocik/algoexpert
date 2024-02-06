# Solution 1
# def longestSubarrayWithSum(array, targetSum):
#     # O(n) time / O(1) space
#     result = []
#     longestLength = 0
#     currentSum = 0
#     currentLength = 0
#     i, j = 0, 0
#     while j < len(array):
#         if currentSum > targetSum:
#             currentSum -= array[i]
#             currentLength -= 1
#             i += 1
#         else:
#             if currentSum == targetSum and currentLength > longestLength:
#                 longestLength = currentLength
#                 result = [i, j - 1]
#             currentSum += array[j]
#             currentLength += 1
#             j += 1
#
#     return result if currentSum != targetSum else [i, j - 1]

# Solution 2
def longestSubarrayWithSum(array, targetSum):
    # O(n) time / O(1) space
    result = []

    currentSum = 0
    startIndex = 0
    endIndex = 0

    while endIndex < len(array):
        currentSum += array[endIndex]

        while startIndex < endIndex and currentSum > targetSum:
            currentSum -= array[startIndex]
            startIndex += 1

        if currentSum == targetSum:
            if len(result) == 0 or result[1] - result[0] < endIndex - startIndex:
                result = [startIndex, endIndex]

        endIndex += 1

    return result

print(longestSubarrayWithSum([1, 2, 3, 4, 3, 3, 1, 2, 1], 10))