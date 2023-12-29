# Solution 1
# def threeNumberSort(array, order):
#     # O(n ^ 2) time / O(1) space
#     orderIndex = len(order) - 1
#     while orderIndex >= 0:
#         boundary = 0
#         arrayIndex = len(array) - 1
#         while arrayIndex >= boundary:
#             if array[arrayIndex] == order[orderIndex]:
#                 move(array, arrayIndex)
#                 boundary += 1
#             else:
#                 arrayIndex -= 1
#
#         orderIndex -= 1
#
#     return array
#
# def move(array, index):
#     while index > 0:
#         array[index - 1], array[index] = array[index], array[index - 1]
#         index -= 1

# Solution 2
# def threeNumberSort(array, order):
#     # O(n) time / O(1) space
#     index = 0
#     for i in range(0, len(array)):
#         if array[i] == order[0]:
#             array[i], array[index] = array[index], array[i]
#             index += 1
#
#     for i in range(index, len(array)):
#         if array[i] == order[1]:
#             array[i], array[index] = array[index], array[i]
#             index += 1
#
#     return array

# Solution 3
def threeNumberSort(array, order):
    # O(n) time / O(1) space
    first = second = 0
    third = len(array) - 1

    while second <= third:
        if array[second] == order[0]:
            array[second], array[first] = array[first], array[second]
            first += 1
            second += 1
        elif array[second] == order[2]:
            array[second], array[third] = array[third], array[second]
            third -= 1
        else:
            second += 1

    return array

print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))