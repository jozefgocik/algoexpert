def removeIslands(matrix):
    # O(n * m) time / O(n * m) space; n = number of rows, m = number of columns
    borders = set()

    # First row
    for j in range(0, len(matrix[0])):
        removeIslandsHelper(matrix, 0, j, borders)
    # Last row
    for j in range(0, len(matrix[-1])):
        removeIslandsHelper(matrix, len(matrix) - 1, j, borders)

    # First column
    for i in range(0, len(matrix)):
        removeIslandsHelper(matrix, i, 0, borders)
    # Last column
    for i in range(0, len(matrix)):
        removeIslandsHelper(matrix, i, len(matrix[i]) - 1, borders)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (i, j) not in borders and matrix[i][j] == 1:
                matrix[i][j] = 0

    return matrix

def removeIslandsHelper(matrix, i, j, borders):
    # Write your code here.
    if i not in range(0, len(matrix)) or j not in range(0, len(matrix[i])) or matrix[i][j] == 0 or (i, j) in borders:
        return

    borders.add((i, j))
    # Right, Bottom, Left, Up
    removeIslandsHelper(matrix, i, j + 1, borders)
    removeIslandsHelper(matrix, i + 1, j, borders)
    removeIslandsHelper(matrix, i, j - 1, borders)
    removeIslandsHelper(matrix, i - 1, j, borders)

print(removeIslands([
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]))