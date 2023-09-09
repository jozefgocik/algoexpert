# Solution 1
# def smallestDifference(arrayOne, arrayTwo):
#     # O(n^2) time / O(1) space
#     result = [0, 0]
#     temp = float("inf")
#     for i in arrayOne:
#         for j in arrayTwo:
#             if i == j:
#                 result[0] = i
#                 result[1] = j
#             elif i > j:
#                 difference = i - j
#                 if difference < temp:
#                     result[0] = i
#                     result[1] = j
#                     temp = difference
#             elif j > i:
#                 difference = j - i
#                 if difference < temp:
#                     result[0] = i
#                     result[1] = j
#                     temp = difference
#
#     return result

# Solution 2
def smallestDifference(arrayOne, arrayTwo):
    # O(n^2) time / O(1) space
    arrayOne.sort()
    arrayTwo.sort()

    result = [0, 0]
    temp = float("inf")

    one = 0
    two = 0
    while one < len(arrayOne) and two < len(arrayTwo):
        if arrayOne[one] == arrayTwo[two]:
            result[0] = arrayOne[one]
            result[1] = arrayTwo[two]
            one += 1
            two += 1
        elif arrayOne[one] > arrayTwo[two]:
            difference = arrayOne[one] - arrayTwo[two]
            if difference < temp:
                result[0] = arrayOne[one]
                result[1] = arrayTwo[two]
                temp = difference
            two += 1
        elif arrayOne[one] < arrayTwo[two]:
            difference = arrayTwo[two] - arrayOne[one]
            if difference < temp:
                result[0] = arrayOne[one]
                result[1] = arrayTwo[two]
                temp = difference
            one += 1

    return result

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
# [28, 26]