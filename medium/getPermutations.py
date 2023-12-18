def getPermutations(array):
    # O(n * n!) time / O(n * n!) space
    permutations = []
    getPermutationsHelper(array, [], permutations)
    return permutations


def getPermutationsHelper(array, permutation, permutations):
    if not array and permutation:
        permutations.append(permutation)
    else:
        for i in range(0, len(array)):
            newArray = array.copy()
            newArray.remove(array[i])
            newPermutation = permutation + [array[i]]
            getPermutationsHelper(newArray, newPermutation, permutations)


print(getPermutations([1, 2, 3]))
