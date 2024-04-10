def diceThrows(numDice, numSides, target):
    # O(d * s * t) time / O(d * t); d = numDice, s = numSides, t = target
    storedResults = [[-1] * (target + 1) for _ in range(numDice + 1)]
    return diceThrowsHelper(numDice, numSides, target, storedResults)


def diceThrowsHelper(numDice, numSides, target, storedResults):
    if numDice == 0:
        return 1 if target == 0 else 0
    if storedResults[numDice][target] > -1:
        return storedResults[numDice][target]

    result = 0
    for i in range(max(0, target - numSides), target):
        result += diceThrowsHelper(numDice - 1, numSides, i, storedResults)
    storedResults[numDice][target] = result

    return result


print(diceThrows(3, 6, 5))
print(diceThrows(2, 6, 7))