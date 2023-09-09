# Solution 1
# def threeNumberSum(array, targetSum):
#     # O(n^3)) time / O(n) space
#     array.sort()
#     result = []
#     for i, num in enumerate(array):
#         for j in range(i+1, len(array)):
#             targetNum = targetSum - (num + array[j])
#             for k in range(j+1, len(array)):
#                 if array[k] == targetNum:
#                     result.append([num, array[j], array[k]])
#
#     return result

# Solution 2
def threeNumberSum(array, targetSum):
    # O(n^2) time / O(n) space
    array.sort()
    result = []
    for i in range(0, len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1

    return result

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
