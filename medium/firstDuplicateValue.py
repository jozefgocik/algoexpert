# Solution 1
# def firstDuplicateValue(array):
#     # O(n) time / O(n) space
#     table = {}
#
#     for i in array:
#         if i in table:
#             return i
#         table[i] = False
#
#     return -1

# Solution 2
def firstDuplicateValue(array):
    # O(n) time / O(1) space
    for i in array:
        absValue = abs(i)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1

    return -1

print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
# 2
