# Solution 1
# def spiralTraverse(array):
#     # O(n) time / O(n) space
#     result = []
#     state = "r"  # r = right, d = down, l = left, u = up,
#
#     i = 0
#     while len(array) > 0:
#         if state == "r":
#             for j, num in enumerate(array[i]):
#                 result.append(num)
#             array.remove(array[i])
#             state = "d"
#             i -= 1
#
#         elif state == "d":
#             for j in range(0, len(array)):
#                 if len(array[j]) > 0:
#                     result.append(array[j][-1])
#                     array[j].pop()
#                 if j == len(array) - 1:
#                     state = "l"
#                 i += 1
#
#         elif state == "l":
#             for j, num in enumerate(array[i][::-1]):
#                 result.append(num)
#             array.remove(array[i])
#             state = "u"
#
#         elif state == "u":
#             for j in range(0, len(array))[::-1]:
#                 if len(array[j]) > 0:
#                     result.append(array[j][0])
#                     array[j].pop(0)
#                 if j == len(array) - 1:
#                     state = "r"
#                 i -= 1
#
#     return result

# Solution 2
# def spiralTraverse(array):
#     # O(n) time / O(n) space
#     result = []
#
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len(array[0]) - 1
#
#     while startRow <= endRow and startCol <= endCol:
#         for col in range(startCol, endCol + 1):
#             result.append(array[startRow][col])
#
#         for row in range(startRow + 1, endRow + 1):
#             result.append(array[row][endCol])
#
#         for col in reversed(range(startCol, endCol)):
#             if startRow == endRow:
#                 break
#             result.append(array[endRow][col])
#
#         for row in reversed(range(startRow + 1, endRow)):
#             if startCol == endCol:
#                 break
#             result.append(array[row][startCol])
#
#         startRow += 1
#         endRow -= 1
#         startCol += 1
#         endCol -= 1
#
#     return result

# Solution 3
def spiralTraverse(array):
    # O(n) time / O(n) space
    result = []
    spiralTraverseHelper(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiralTraverseHelper(array, startRow, endRow, startCol, endCol, result):
    # O(n) time / O(n) space
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        if startCol == endCol:
            break
        result.append(array[row][startCol])

    spiralTraverseHelper(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)

print(spiralTraverse([
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7]
]))
print(spiralTraverse(
    [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6]
    ]
))
print(spiralTraverse([
    [27, 12, 35, 26],
    [25, 21, 94, 11],
    [19, 96, 43, 56],
    [55, 36, 10, 18],
    [96, 83, 31, 94],
    [93, 11, 90, 16]
]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]