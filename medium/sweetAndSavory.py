# dish > 0 => savory
# dish < 0 => sweet
# abs(dish) => intensity
# If no valid solution => return [0, 0]
def sweetAndSavory(dishes, target):
    # O(nLog(n)) time / O(n) space
    sweets = sorted([dish for dish in dishes if dish < 0], key=abs)
    savories = sorted([dish for dish in dishes if dish > 0])

    sweet = 0
    savory = 0
    difference = float("inf")
    sweetIndex = 0
    savoryIndex = 0

    while sweetIndex < len(sweets) and savoryIndex < len(savories):
        currentSum = sweets[sweetIndex] + savories[savoryIndex]

        if currentSum <= target:
            currentDifference = target - currentSum
            if currentDifference < difference:
                difference = currentDifference
                sweet = sweets[sweetIndex]
                savory = savories[savoryIndex]
            savoryIndex += 1
        else:
            sweetIndex += 1

    return [sweet, savory]

print(sweetAndSavory(dishes=[-3, -5, 1, 7], target=8))
# [-3, 7]
print(sweetAndSavory(dishes=[3, 5, 7, 2, 6, 8, 1], target=10))
# [0, 0]
print(sweetAndSavory(dishes=[2, 5, -4, -7, 12, 100, -25], target=-20))
# [-25, 5]