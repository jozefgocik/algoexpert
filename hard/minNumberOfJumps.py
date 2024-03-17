# Solution 1
# def minNumberOfJumps(array):
#     # O(n ^ 2) time / O(1) space
#     result = 0
#
#     i = 0
#     while i < len(array):
#         bestValue = 0
#         bestIdx = -1
#         for j in range(i + 1, i + array[i] + 1):
#             if j >= len(array):
#                 return result
#             current = array[j] + (j - i - 1)
#             if j >= len(array) - 1:
#                 return result + 1
#             if current >= bestValue:
#                 bestValue = current
#                 bestIdx = j
#
#         i = bestIdx
#         result += 1

# Solution 2
def minNumberOfJumps(array):
    # O(n) time / O(1) space
    result = 0

    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array)):
        if i == len(array) - 1:
            return result + 1

        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        if steps == 0:
            result += 1
            steps = maxReach - i

    return result


print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
print(minNumberOfJumps([1]))
