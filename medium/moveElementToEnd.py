# Solution 1
# def moveElementToEnd(array, toMove):
#     # O(n^2) time / O(1) space
#     for i in array:
#         if i == toMove:
#             array.remove(i)
#             array.append(i)
#
#     return array

# Solution 2
def moveElementToEnd(array, toMove):
    # O(n) time / O(1) space
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
        elif array[left] != toMove and array[right] == toMove:
            right -= 1
        elif array[left] != toMove and array[right] != toMove:
            left += 1
        else:
            right -= 1

    return array
print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
# [4, 1, 3, 2, 2, 2, 2, 2]