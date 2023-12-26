# Solution 1
# def staircaseTraversal(height, maxSteps):
#     # O(m ^ h) time / O(h) space; m = maxSteps, h = height
#     return staircaseTraversalHelper(height, maxSteps)
#
# def staircaseTraversalHelper(height, maxSteps):
#     if height == 1 or height == 0:
#         return 1
#     else:
#         result = 0
#         for i in range(1, min(maxSteps, height) + 1):
#             result += staircaseTraversalHelper(height - i, maxSteps)
#         return result

# Solution 2
# def staircaseTraversal(height, maxSteps):
#     # O(m * h) time / O(h) space; m = maxSteps, h = height
#     return staircaseTraversalHelper(height, maxSteps, {0: 1, 1: 1})
#
# def staircaseTraversalHelper(height, maxSteps, hashmap):
#     if height in hashmap:
#         return hashmap[height]
#     else:
#         result = 0
#         for i in range(1, min(maxSteps, height) + 1):
#             result += staircaseTraversalHelper(height - i, maxSteps, hashmap)
#
#         hashmap[height] = result
#
#         return result

# Solution 3
# def staircaseTraversal(height, maxSteps):
#     # O(m * h) time / O(h) space; m = maxSteps, h = height
#     result = [0 for _ in range(0, height + 1)]
#     result[0] = 1
#     result[1] = 1
#
#     for i in range(2, len(result)):
#         num = 0
#         for j in range(1, min(maxSteps, i) + 1):
#             num += result[i - j]
#         result[i] = num
#
#     return result[height]

# Solution 4
def staircaseTraversal(height, maxSteps):
    # O(h) time / O(h) space; h = height
    currentNunmberOfWays = 0
    result = [1]

    for currentHeight in range(1, height + 1):
        start = currentHeight - maxSteps - 1
        end = currentHeight - 1
        if start >= 0:
            currentNunmberOfWays -= result[start]

        currentNunmberOfWays += result[end]
        result.append(currentNunmberOfWays)

    return result[height]

# 5
print(staircaseTraversal(4, 2))