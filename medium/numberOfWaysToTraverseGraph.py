# Solution 1
# def numberOfWaysToTraverseGraph(width, height):
#     # O(n * m) time / O(n * m) space; n = width, m = height
#     array = [[0 for x in range(0, width)] for y in range(0, height)]
#     array[height - 1][width - 1] = -1
#
#     return numberOfWaysToTraverseGraphHelper(width, height, array)
#
#
# def numberOfWaysToTraverseGraphHelper(width, height, array, x=0, y=0):
#     if array[x][y] != 0:
#         if array[x][y] == -1:
#             array[x][y] += 1
#         array[x][y] += 1
#         return
#
#     if x < height - 1:
#         numberOfWaysToTraverseGraphHelper(width, height, array, x + 1, y)
#     if y < width - 1:
#         numberOfWaysToTraverseGraphHelper(width, height, array, x, y + 1)
#
#     return array[-1][-1]

# Solution 2
# def numberOfWaysToTraverseGraph(width, height):
#     # O(2^(n + m)) time / O(n + m); n = width, m = height
#     if width == 1 or height == 1:
#         return 1
#
#     left = numberOfWaysToTraverseGraph(width - 1, height)
#     up = numberOfWaysToTraverseGraph(width, height - 1)
#
#     return left + up

# Solution 3
def numberOfWaysToTraverseGraph(width, height):
    # O(n * m) time / O(n * m) space; n = width, m = height
    numberOfWays = [[0 for _ in range(0, width + 1)] for _ in range(0, height + 1)]

    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                a = numberOfWays[heightIdx - 1][widthIdx]
                b = numberOfWays[heightIdx][widthIdx - 1]
                numberOfWays[heightIdx][widthIdx] = a + b

    return numberOfWays[height][width]

print(numberOfWaysToTraverseGraph(2, 3))