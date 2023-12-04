#Solution 1
# def validStartingCity(distances, fuel, mpg):
#     # O(n^2) time / O(1) space
#     for i in range(0, len(distances)):
#         index = 0
#         currentFuel = 0
#         while index < len(distances):
#             if currentFuel < 0:
#                 break
#             if i + index < len(distances):
#                 currentFuel += fuel[i + index] * mpg
#                 currentFuel -= distances[i + index]
#             else:
#                 currentFuel += fuel[i + index - len(distances)] * mpg
#                 currentFuel -= distances[i + index - len(distances)]
#             index += 1
#
#         if currentFuel >= 0:
#             return i
#
#     return -1

#Solution 2
def validStartingCity(distances, fuel, mpg):
    # O(n) time / O(1) space
    index = 0
    minValue = 0
    currentFuel = 0
    for i in range(0, len(distances)):
        if currentFuel < minValue:
            minValue = currentFuel
            index = i

        currentFuel += fuel[i] * mpg
        currentFuel -= distances[i]

    return index

print(validStartingCity([5, 25, 15, 10, 15],[1, 2, 1, 0, 3],10))