# Solution 1
# def maxSubsetSumNoAdjacent(array):
#     # O(n) time / O(n) space
#     if not array:
#         return 0
#
#     maxSums = []
#     for i in range(0, len(array)):
#         if i == 0:
#             maxSums.append(array[i])
#         elif i == 1:
#             maxSums.append(max(array[i], array[i-1]))
#         else:
#             maxSums.append(max(maxSums[i-1], maxSums[i-2] + array[i]))
#
#     return maxSums[-1]

# Solution 2
def maxSubsetSumNoAdjacent(array):
    # O(n) time / O(1) space
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]

    first = array[0]
    second = max(array[0], array[1])
    maxSum = second
    for i in range(2, len(array)):
        maxSum = max(second, first + array[i])
        first = second
        second = maxSum

    return maxSum

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))