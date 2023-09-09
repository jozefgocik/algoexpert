#Solution 1
# def majorityElement(array):
#     # O(n^2) time / O(1) space
#     for i in array:
#         if array.count(i) >= len(array) / 2:
#             return i
#
#     return -1

# Solution 2
# def majorityElement(array):
#     # O(n) time / O(1) space
#     index = 0
#     element = -1
#     while element == -1:
#         counter = 0
#         for i in array:
#             if array[index] == i:
#                 counter += 1
#         if counter >= len(array) / 2:
#             element = array[index]
#         else:
#             index += 1
#
#     return element

# Solution 3
def majorityElement(array):
    # O(n) time / O(1) space
    counter = 0
    element = -1

    for i in array:
        if counter == 0:
            element = i

        if element == i:
            counter += 1
        else:
            counter -= 1

    return element

print(majorityElement([2]))
# 2
print(majorityElement([1, 2, 3, 2, 2, 1, 2]))
# 2