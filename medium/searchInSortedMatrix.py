# Solution 1
# def searchInSortedMatrix(matrix, target):
#     # O(n * m) time / O(1) space; n = height of matrix, m = width of matrix
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             if matrix[i][j] == target:
#                 return [i, j]
#
#     return [-1, -1]

# Solution 2
# def searchInSortedMatrix(matrix, target):
#     # O(n * m) time / O(1) space; n = height of matrix, m = width of matrix
#     row = 0
#     column = 0
#
#     while row < len(matrix) and matrix[row][0] <= target:
#         row += 1
#
#     while column < len(matrix[0]) and matrix[0][column] <= target:
#         column += 1
#
#     for i in range(0, row):
#         for j in range(0, column):
#             if matrix[i][j] == target:
#                 return [i, j]
#
#     return [-1, -1]

# Solution 3
def searchInSortedMatrix(matrix, target):
    # O(n + m) time / O(1) space; n = height of matrix, m = width of matrix
    row = 0
    column = len(matrix[row]) - 1
    while row < len(matrix) and column >= 0:
        if matrix[row][column] > target:
            column -= 1
        elif matrix[row][column] < target:
            row += 1
        else:
            return [row, column]

    return [-1, -1]

print(searchInSortedMatrix(
[
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
], 44
))