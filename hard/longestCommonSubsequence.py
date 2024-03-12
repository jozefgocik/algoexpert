# Solution 1
# def longestCommonSubsequence(str1, str2):
#     # O(n * m * min(n, m)) time / O(n * m * min(n, m)) space; n = len(str1), m = len(str2)
#     result = [[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
#
#     for row in range(1, len(str2) + 1):
#         for col in range(1, len(str1) + 1):
#             if str2[row - 1] == str1[col - 1]:
#                 topLeft = result[row - 1][col - 1]
#                 result[row][col] = topLeft + [str2[row - 1]]
#             else:
#                 left = result[row][col - 1]
#                 top = result[row - 1][col]
#                 result[row][col] = left if len(left) >= len(top) else top
#
#     return result[-1][-1]

# Solution 2
def longestCommonSubsequence(str1, str2):
    # O(n * m) time / O(n * m) space
    result = [[[None, 0, None, None] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                result[i][j] = [str2[i - 1], result[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if result[i - 1][j][1] > result[i][j - 1][1]:
                    result[i][j] = [None, result[i - 1][j][1], i - 1, j]
                else:
                    result[i][j] = [None, result[i][j - 1][1], i, j - 1]

    return buildSequence(result)

def buildSequence(array):
    sequnce = []
    i = len(array) - 1
    j = len(array[0]) - 1

    while i != 0 and j != 0:
        current = array[i][j]
        if current[0] is not None:
            sequnce.append(current[0])
        i = current[2]
        j = current[3]

    return sequnce[::-1]


# ["X", "Y", "Z" ,"W"]
print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))
