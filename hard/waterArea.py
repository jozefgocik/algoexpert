# Solution 1
# def waterArea(heights):
#     # O(n ^ 2) time / O(1) space
#     result = 0
#
#     i = 0
#     while i < len(heights):
#         if heights[i] != 0:
#             leftIdx = i
#             rightIdx = len(heights) - 1
#             squareArea = 0
#             j = len(heights) - 1
#             while j > leftIdx:
#                 if heights[j] >= heights[leftIdx] or heights[j] >= heights[rightIdx]:
#                     rightIdx = j
#                     squareArea = 0
#                 else:
#                     squareArea += min(heights[leftIdx], heights[rightIdx]) - heights[j]
#                 j -= 1
#
#             result += squareArea
#             i = rightIdx
#
#             if rightIdx == len(heights) - 1:
#                 return result
#         else:
#             i += 1
#
#     return result

# Solution 2
def waterArea(heights):
    # O(n) time / O(n) space
    maxes = [0 for _ in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)

    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(maxes[i], rightMax)
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)

    return sum(maxes)


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
