# Solution 1
# def sunsetViews(buildings, direction):
#     # O(n ^ 2) time / O(n) space
#     result = []
#     for i in range(0, len(buildings)):
#         result.append(i)
#         j = i + 1 if direction == "EAST" else i - 1
#         while j < len(buildings) if direction == "EAST" else j >= 0:
#             if buildings[i] <= buildings[j]:
#                 result.pop()
#                 break
#             j = j + 1 if direction == "EAST" else j - 1
#
#
#     return result

# Solution 2
def sunsetViews(buildings, direction):
    # O(n) time / O(n) space
    result = []
    tallest = float("-inf")
    for i in reversed(range(0, len(buildings))) if direction == "EAST" else range(0, len(buildings)):
        if buildings[i] > tallest:
            tallest = buildings[i]
            result.append(i)

    return result[::-1] if direction == "EAST" else result

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))