def riverSizes(matrix):
    # O(n * m) time / O(n * m) space; n = number of rows, m = number of columns
    result = []
    visited = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (i, j) not in visited and matrix[i][j] == 1:
                result.append(riverSizesHelper(matrix, i, j, visited))

    return result

def riverSizesHelper(matrix, i, j, visited):
    if i not in range(0, len(matrix)) or j not in range(0, len(matrix[i])) or matrix[i][j] == 0 or (i, j) in visited:
        return 0

    visited.add((i, j))
    length = 0

    # Right, Bottom, Left, Up
    length += riverSizesHelper(matrix, i, j + 1, visited)
    length += riverSizesHelper(matrix, i + 1, j, visited)
    length += riverSizesHelper(matrix, i, j - 1, visited)
    length += riverSizesHelper(matrix, i - 1, j, visited)

    return length + 1

# [2, 1, 5, 2, 2]
print(riverSizes([
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]))

# [3, 5, 6]
print(riverSizes([
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1]
]))