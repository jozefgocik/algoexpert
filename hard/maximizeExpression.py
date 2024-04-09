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
    # O(n) time / O(n) space
    if len(array) < 4:
        return 0

    maxA = [array[0]]
    for i in range(1, len(array)):
        maxA.append(max(maxA[i - 1], array[i]))

    maxAMinusB = [None, maxA[0] - array[1]]
    for i in range(2, len(array)):
        maxAMinusB.append(max(maxAMinusB[i - 1], maxA[i - 1] - array[i]))

    maxAMinusBPlusC = [None,  None, maxAMinusB[1] + array[2]]
    for i in range(3, len(array)):
        maxAMinusBPlusC.append(max(maxAMinusBPlusC[i - 1], maxAMinusB[i - 1] + array[i]))

    maxAMinusBPlusCMinusD = [None, None, None, maxAMinusBPlusC[2] - array[3]]
    for i in range(4, len(array)):
        maxAMinusBPlusCMinusD.append(max(maxAMinusBPlusCMinusD[i - 1], maxAMinusBPlusC[i - 1] - array[i]))

    return maxAMinusBPlusCMinusD[-1]


print(maximizeExpression([3, 6, 1, -3, 2, 7]))
# array[a] - array[b] + array[c] - array[d]
# [1, -30, 6, 1, -3, 2, 7]