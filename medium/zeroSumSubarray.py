# Solution 1
# def zeroSumSubarray(nums):
#     # O(n^2) time / O(1) space
#     for i in range(0, len(nums)):
#         currentNum = nums[i]
#         if currentNum == 0:
#             return True
#         for j in range(i + 1, len(nums)):
#             currentNum += nums[j]
#             if currentNum == 0:
#                 return True
#
#     return False

# Solution 2
def zeroSumSubarray(nums):
    # O(n) time / O(n) space
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)

    return False

print(zeroSumSubarray([-5, -5, 2, 3, -2]))
# True => [-5, 2, 3] = 0