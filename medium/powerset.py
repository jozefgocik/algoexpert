# Solution 1
# def powerset(array):
#     # O((2 ^ n) * n) / ((2 ^ n) * n) space
#     subsets = [[]]
#     for element in array:
#         for i in range(0, len(subsets)):
#             currentSubset = subsets[i]
#             subsets.append(currentSubset + [element])
#
#     return subsets

# Solution 2
def powerset(array, index = None):
    # O((2 ^ n) * n) / ((2 ^ n) * n) space
    if index is None:
        index = len(array) - 1
    if index < 0:
        return [[]]

    element = array[index]
    subsets = powerset(array, index - 1)
    for i in range(0, len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [element])

    return subsets

print(powerset([1, 2, 3]))