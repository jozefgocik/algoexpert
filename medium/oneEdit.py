# Solution 1
# def oneEdit(stringOne, stringTwo):
#     # O(n) time / O(1) space
#     if stringOne == stringTwo:
#         return True
#
#     if abs(len(stringOne) - len(stringTwo)) > 1:
#         return False
#
#     result = 0
#     if len(stringOne) == len(stringTwo):
#         index = 0
#         for i in range(len(stringOne)):
#             if stringOne[index] != stringTwo[index]:
#                 result += 1
#             index += 1
#     else:
#         indexOne = 0
#         indexTwo = 0
#         longer = 1 if len(stringOne) > len(stringTwo) else 2
#         for i in range(max(len(stringOne), len(stringTwo))):
#             if indexOne >= len(stringOne) or indexTwo >= len(stringTwo) or stringOne[indexOne] != stringTwo[indexTwo]:
#                 indexOne += 1 if longer == 1 else 0
#                 indexTwo += 1 if longer == 2 else 0
#                 result += 1
#             else:
#                 indexOne += 1
#                 indexTwo += 1
#
#     return result < 2

# Solution 2
def oneEdit(stringOne, stringTwo):
    # O(n) time / O(1) space
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)

    if abs(lengthOne - lengthTwo) > 1:
        return False

    madeEdit = False
    indexOne = 0
    indexTwo = 0

    while indexOne < lengthOne and indexTwo < lengthTwo:
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if madeEdit:
                return False
            madeEdit = True

            if lengthOne > lengthTwo:
                indexOne += 1
            elif lengthTwo > lengthOne:
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1

        else:
            indexOne += 1
            indexTwo += 1

    return True


print(oneEdit("hello", "hollo"))
print(oneEdit("hello", "hllo"))
print(oneEdit("hello", "ellos"))
