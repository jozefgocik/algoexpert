# Solution 1
# def kadanesAlgorithm(array):
#     # O(n^2) time / O(1) Space
#     maxSum = float("-inf")
#     for i in range(0, len(array)):
#         currentSum = array[i]
#         for j in range(i + 1, len(array)):
#             if currentSum > maxSum:
#                 maxSum = currentSum
#             currentSum += array[j]
#
#         maxSum = currentSum if currentSum > maxSum else maxSum
#         currentSum = 0
#
#     return maxSum

# Solution 2
def kadanesAlgorithm(array):
    # O(n) time / O(1) space
    maxSum = array[0]
    currentSum = array[0]
    for i in range(1, len(array)):
        currentSum = max(array[i] + currentSum, array[i])
        if currentSum > maxSum:
            maxSum = currentSum

    return maxSum

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))