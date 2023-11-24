# Solution 1
# def minimumPassesOfMatrix(matrix):
#     # O(w * h * max(w, h)) time / O(w * h) space; w = width, h = height of the matrix
#     negativeValues = 0
#     for i in matrix:
#         for j in i:
#             if j < 0:
#                 negativeValues += 1
#
#     result = 0
#     visited = set()
#
#     negativeValuesPreviously = negativeValues
#     while negativeValues > 0:
#         negativeValues = 0
#         visited.clear()
#         for i in range(0, len(matrix)):
#             for j in range(0, len(matrix[i])):
#                 if matrix[i][j] < 0:
#                     if i - 1 in range(0, len(matrix)) and matrix[i - 1][j] > 0 and (i - 1, j) not in visited:
#                         matrix[i][j] *= -1
#                         visited.add((i, j))
#                     elif i + 1 in range(0, len(matrix)) and matrix[i + 1][j] > 0 and (i + 1, j) not in visited:
#                         matrix[i][j] *= -1
#                         visited.add((i, j))
#                     elif j - 1 in range(0, len(matrix[i])) and matrix[i][j - 1] > 0 and (i, j - 1) not in visited:
#                         matrix[i][j] *= -1
#                         visited.add((i, j))
#                     elif j + 1 in range(0, len(matrix[i])) and matrix[i][j + 1] > 0 and (i, j + 1) not in visited:
#                         matrix[i][j] *= -1
#                         visited.add((i, j))
#                     else:
#                         negativeValues += 1
#
#         if negativeValues == negativeValuesPreviously:
#             return -1
#         else:
#             negativeValuesPreviously = negativeValues
#
#         result += 1
#
#     return result

# Solution 2
def minimumPassesOfMatrix(matrix):
    # O(w * h) time / O(w * h) space; w = width, h = height of the matrix
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    nextPassQueue = getAllPositivePositions(matrix)

    passes = 0
    while len(nextPassQueue) > 0:
        currentPassQueue = nextPassQueue
        nextPassQueue = []

        while len(currentPassQueue) > 0:
            currentRow, currentCol = currentPassQueue.pop(0)

            adjacentPositions = getAdjacentPositions(matrix, currentRow, currentCol)
            for position in adjacentPositions:
                row, col = position
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    nextPassQueue.append([row, col])

        passes += 1

    return passes

def getAllPositivePositions(matrix):
    positivePositions = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            value = matrix[i][j]
            if value > 0:
                positivePositions.append([i, j])

    return positivePositions

def getAdjacentPositions(matrix, row, col):
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row - 1, col])
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])
    if col > 0:
        adjacentPositions.append([row, col - 1])
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])

    return adjacentPositions

def containsNegative(matrix):
    for i in matrix:
        for j in i:
            if j < 0:
                return True

    return False

print(minimumPassesOfMatrix([
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]))
