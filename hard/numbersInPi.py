def numbersInPi(pi, numbers):
    # O(n ^ 3 + m) time / O(n + m) space; n = len(pi), m = len(numbers)
    numberSet = set(numbers)
    minSpaces = numbersInPiHelper(pi, numberSet, {}, 0)

    return -1 if minSpaces == float("inf") else minSpaces


def numbersInPiHelper(pi, numbers, cache, index):
    if index == len(pi):
        return -1
    if index in cache:
        return cache[index]

    minSpaces = float("inf")
    for i in range(index, len(pi)):
        prefix = pi[index:i+1]
        if prefix in numbers:
            minSpacesInSuffix = numbersInPiHelper(pi, numbers, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)

    cache[index] = minSpaces
    return minSpaces


print(numbersInPi("3141592653589793238462643383279",
                  ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]))