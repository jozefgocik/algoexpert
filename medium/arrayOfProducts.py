# Solution 1
# def arrayOfProducts(array):
#     # O(n^2) time / O(n) space
#     result = []
#
#     for i in range(0, len(array)):
#         currentValue = 1
#         for j in range(0, len(array)):
#             if i != j:
#                 currentValue *= array[j]
#         result.append(currentValue)
#
#     return result

# Solution 2
# def arrayOfProducts(array):
#     # O(n^2) time / O(n) space
#     result = []
#
#     for i in range(0, len(array)):
#         currentValue = 1
#
#         left = i - 1
#         while left >= 0:
#             currentValue *= array[left]
#             left -= 1
#
#         right = i + 1
#         while right < len(array):
#             currentValue *= array[right]
#             right += 1
#
#         result.append(currentValue)
#
#     return result

# Solution 3
def arrayOfProducts(array):
    # O(n) time / O(n) space
    result = [1 for _ in range(0, len(array))]

    left = 1
    for i in range(0, len(array)):
        result[i] = left
        left *= array[i]

    right = 1
    for i in reversed(range(0, len(array))):
        result[i] *= right
        right *= array[i]

    return result

print(arrayOfProducts([5, 1, 4, 2]))
# [8, 40, 10, 20]