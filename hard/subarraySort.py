# Solution 1
# def subarraySort(array):
#     # O(n * log(n)) time / O(n) space
#     sortedArray = sorted(array)
#     if sortedArray == array:
#         return [-1, -1]
#
#     left = 0
#     while left < len(array):
#         if array[left] != sortedArray[left]:
#             break
#         left += 1
#
#     right = len(array) - 1
#     while right > left:
#         if array[right] != sortedArray[right]:
#             break
#         right -= 1
#
#     return [left, right]

# Solution 2
# def subarraySort(array):
#     # O(n) time / O(1) space
#
#     left = 0
#     while left < len(array) - 1:
#         if array[left] <= array[left + 1]:
#             left += 1
#         else:
#             break
#
#     last = len(array) - 1
#     while last > left:
#         while left > 0 and array[left - 1] > array[last]:
#             left -= 1
#         last -= 1
#
#     right = len(array) - 1
#     while right > 1:
#         if array[right] > array[right - 1]:
#             right -= 1
#         else:
#             break
#
#     first = 0
#     while first < right:
#         while right < len(array) - 1 and array[right + 1] < array[first]:
#             right += 1
#         first += 1
#
#     return [-1, -1] if left >= right else [left, right]

# Solution 3
def subarraySort(array):
    # O(n) time / O(1) space
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    if minOutOfOrder == float("inf") or maxOutOfOrder == float("-inf"):
        return [-1, -1]

    left = 0
    while array[left] <= minOutOfOrder:
        left += 1

    right = len(array) - 1
    while array[right] >= maxOutOfOrder:
        right -= 1

    return [left, right]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return num > array[i + 1] or num < array[i - 1]


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
