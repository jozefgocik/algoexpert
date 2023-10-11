def numberOfWaysToMakeChange(n, denoms):
    # O(n * d) time / O(n) space; d = number of denoms
    ways = [0 for amount in range(0, n + 1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]

    return ways[n]

print(numberOfWaysToMakeChange(6, [1, 5]))