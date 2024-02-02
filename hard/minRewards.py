# Solution 1
# def minRewards(scores):
#     # O(n ^ 2) time / O(n) space
#     result = []
#
#     for i in range(len(scores)):
#         if not result:
#             result.append(1)
#         elif scores[i - 1] > scores[i]:
#             result.append(1)
#             j = i
#             while j > 0 and scores[j - 1] > scores[j]:
#                 while result[j - 1] <= result[j]:
#                     result[j - 1] += 1
#                 j -= 1
#         else:
#             result.append(result[-1] + 1)
#
#     return sum(result)

# Solution 2
# def minRewards(scores):
#     # O(n) time / O(n) space
#     result = [1 for _ in range(len(scores))]
#
#     if len(result) <= 1:
#         return sum(result)
#
#     for i in range(len(scores)):
#         if i == 0 and scores[i] < scores[i + 1]:
#             minRewardsHelper(scores, result, i)
#         elif i == len(scores) - 1 and scores[i] < scores[i - 1]:
#             minRewardsHelper(scores, result, i)
#         elif scores[i] < scores[i - 1] and scores[i] < scores[i + 1]:
#             minRewardsHelper(scores, result, i)
#
#     return sum(result)
#
#
# def minRewardsHelper(scores, result, i):
#     if i != 0:
#         left = i
#         while left > 0 and scores[left - 1] > scores[left]:
#             result[left - 1] = max(result[left - 1], result[left] + 1)
#             left -= 1
#     if i != len(scores) - 1:
#         right = i
#         while right < len(scores) - 1 and scores[right] < scores[right + 1]:
#             result[right + 1] = max(result[right + 1], result[right] + 1)
#             right += 1

# Solution 3
def minRewards(scores):
    # O(n) time / O(n) space
    result = [1 for _ in range(len(scores))]

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            result[i] = result[i - 1] + 1

    for i in reversed(range(0, len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            result[i] = max(result[i], result[i + 1] + 1)

    return sum(result)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
