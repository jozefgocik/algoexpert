def fourNumberSum(array, targetSum):
    # O(n ^ 2) time / O(n ^ 2) space
    result = []
    table = {}

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            desiredSum = targetSum - (array[i] + array[j])
            if desiredSum in table:
                for l in table[desiredSum]:
                    quadruplet = l + [array[i], array[j]]
                    result.append(quadruplet)
        for k in range(i):
            if (array[i] + array[k]) not in table:
                table[array[i] + array[k]] = []
            table[array[i] + array[k]].append([array[i], array[k]])

    return result


print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
