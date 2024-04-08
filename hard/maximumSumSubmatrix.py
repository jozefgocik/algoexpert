# Solution 1
# def maximumSumSubmatrix(matrix, size):
#     # O(n * m * (size ^ 2)) time / O(1) space; n = height, m = width
#     result = float("-inf")
#     left = 0
#     right = size
#
#     for row in range(len(matrix) - size + 1):
#         while right <= len(matrix[0]):
#             currentSum = 0
#             currentRow = row
#             while currentRow < len(matrix) and currentRow < row + size:
#                 for col in range(left, right):
#                     currentSum += matrix[currentRow][col]
#                 currentRow += 1
#
#             result = max(result, currentSum)
#             left += 1
#             right += 1
#
#         left = 0
#         right = size
#
#     return result

# Solution 2
def maximumSumSubmatrix(matrix, size):
    # O(n * m) time / O(n * m) space; n = height; m = width
    sums = [[0 for col in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    # Initialize first col
    for row in range(1, len(sums)):
        sums[row][0] = matrix[row][0] + sums[row - 1][0]
    # Initialize first row
    for col in range(1, len(sums[0])):
        sums[0][col] = matrix[0][col] + sums[0][col - 1]
    # Initialize rest of the array
    for row in range(1, len(sums)):
        for col in range(1, len(sums[row])):
            sums[row][col] = matrix[row][col] + sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1]

    maxSum = float("-inf")
    for row in range(size - 1, len(sums)):
        for col in range(size - 1, len(sums[row])):
            total = sums[row][col]

            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]

            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]

            if not touchesTopBorder and not touchesLeftBorder:
                total += sums[row - size][col - size]

            maxSum = max(maxSum, total)

    return maxSum


print(maximumSumSubmatrix([
  [5, 3, -1, 5],
  [-7, 3, 7, 4],
  [12, 8, 0, 0],
  [1, -8, -8, 2]
], 2
))