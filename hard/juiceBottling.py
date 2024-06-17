def juiceBottling(prices):
    # O(n ^ 3) time / O(n ^ 2) space
    maxProfit = [0] * len(prices)
    solutions = [[]] * len(prices)
    for quantity in range(len(prices)):
        for dividingPoint in range(quantity + 1):
            possibleProfit = maxProfit[quantity - dividingPoint] + prices[dividingPoint]

            if possibleProfit > maxProfit[quantity]:
                maxProfit[quantity] = possibleProfit
                solutions[quantity] = [dividingPoint] + solutions[quantity - dividingPoint]

    return solutions[-1]


print(juiceBottling([0, 1]))
