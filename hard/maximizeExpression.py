# Solution 1
# def maximizeExpression(array):
#     # O(n ^ 4) time / O(1) space
#     if len(array) < 4:
#         return 0
#
#     maxSum = float("-inf")
#     a, b, c, d = 0, 1, 2, 3
#     while a < len(array) - 3:
#         while d < len(array):
#             currentSum = array[a] - array[b] + array[c] - array[d]
#             maxSum = max(maxSum, currentSum)
#             d += 1
#
#         if b == len(array) - 3:
#             a += 1
#             b = a + 1
#             c = b + 1
#             d = c + 1
#         elif c == len(array) - 2:
#             b += 1
#             c = b + 1
#             d = c + 1
#         else:
#             c += 1
#             d = c + 1
#
#     return maxSum

# Solution 2
def maximizeExpression(array):
    # Write your code here.
    return -1


print(maximizeExpression([3, 6, 1, -3, 2, 7]))
# array[a] - array[b] + array[c] - array[d]
# [1, -30, 6, 1, -3, 2, 7]