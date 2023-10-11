def minNumberOfCoinsForChange(n, denoms):
    # O(n * d) time / O(n) space; d = number of denoms
    array = [float("inf") for amount in range(0, n + 1)]
    array[0] = 0

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                array[amount] = min(array[amount], 1 + array[amount - denom])

    return array[n] if array[n] != float("inf") else -1

if __name__ == '__main__':
    print(minNumberOfCoinsForChange(7, [1, 5, 10]))