def blackjackProbability(target, startingHand):
    # O(t - s) time / O(t - s) space; t = target, s = startingHand
    memo = {}
    return round(blackjackProbabilityHelper(target, startingHand, memo), 3)

def blackjackProbabilityHelper(target, currentHand, memo):
    # Write your code here.
    if currentHand in memo:
        return memo[currentHand]
    if currentHand > target:
        return 1
    if currentHand + 4 >= target:
        return 0

    result = 0
    for i in range(1, 11):
        result += 0.1 * blackjackProbabilityHelper(target, currentHand + i, memo)

    memo[currentHand] = result
    return result

print(blackjackProbability(21, 15))