# Solution 1
# def missingNumbers(nums):  # n = len(nums) + 2
#     # O(nLog(n)) time / O(n) space
#     nums.sort()
#
#     result = []
#     counter = 0
#     for i in range(1,  len(nums) + 3):
#         if counter < len(nums) and nums[counter] == i:
#             counter += 1
#         else:
#             result.append(i)
#
#     return result

# Solution 2
def missingNumbers(nums):  # n = len(nums) + 2
    # O(n) time / O(n) space
    includedNums = set(nums)

    result = []
    for i in range(1,  len(nums) + 3):
        if i not in includedNums:
            result.append(i)

    return result

print(missingNumbers([1, 4, 3]))
# [2, 5] => n is 5, meaning the completed list should be [1, 2, 3, 4, 5]
