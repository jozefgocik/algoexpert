# Solution 1
# def largestRange(array):
#     # O(n * log(n)) time / O(n) space
#     array.sort()
#     result = []
#     currentArray = []
#     for num in array:
#         if not currentArray:
#             currentArray.append(num)
#         else:
#             if num != currentArray[-1]:
#                 if num != currentArray[-1] + 1:
#                     result = currentArray.copy() if len(result) < len(currentArray) else result
#                     currentArray.clear()
#                 currentArray.append(num)
#
#     return [result[0], result[-1]] if len(result) > len(currentArray) else [currentArray[0], currentArray[-1]]

# Solution 2
# def largestRange(array):
#     # O(n) time / O(n) space
#     nums = {}
#     for num in array:
#         if num not in nums:
#             nums[num] = False
#
#     result = []
#     for key, value in nums.items():
#         if not value:
#             nums[key] = True
#             left = key - 1
#             while left in nums:
#                 nums[left] = True
#                 left -= 1
#             left += 1
#
#             right = key + 1
#             while right in nums:
#                 nums[right] = True
#                 right += 1
#             right -= 1
#
#             if not result:
#                 result = [left, right]
#             elif abs(result[-1] - result[0]) < abs(right - left):
#                 result = [left, right]
#
#     return result

# Solution 3
def largestRange(array):
    # O(n) time / O(n) space
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue

        nums[num] = False
        currentLength = 1
        left = num - 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1

        right = num + 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1

        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]

    return bestRange


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
