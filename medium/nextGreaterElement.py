# Solution 1
# def nextGreaterElement(array):
#     # O(n ^ 2) time / O(n) space
#     result = []
#
#     for i in range(0, len(array)):
#         greaterElement = -1
#         j = 0
#         index = i
#         while j < len(array):
#             if array[index%len(array)] > array[i]:
#                 greaterElement = array[index%len(array)]
#                 break
#             index += 1
#             j += 1
#
#         result.append(greaterElement)
#
#     return result

# Solution 2
def nextGreaterElement(array):
    # O(n) time / O(n) space
    result = [-1 for _ in range(len(array))]
    stack = []
    for i in range(2 * len(array)):
        index = i % len(array)
        while stack:
            if array[index] > array[stack[-1]]:
                result[stack[-1]] = array[index]
                stack.pop()
            else:
                break

        stack.append(index)

    return result

print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))