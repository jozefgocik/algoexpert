# Solution 1
# def generateDocument(characters, document):
#     # O(m + n) time / O(m) space
#     chars = []  # m space
#     for i in characters:  # m time
#         chars.append(i)
#
#     for i in document: # n
#         if i not in chars:
#             return False
#         else:
#             chars.remove(i)
#
#     return True

# Solution 2
def generateDocument(characters, document):
    # O(m + n) time / O(c) space
    chars = {}  # c space
    for i in characters:  # m time
        if i not in chars:
            chars[i] = 0
        chars[i] += 1

    for i in document: # n
        if i not in chars or chars[i] < 1:
            return False
        else:
            chars[i] -= 1

    return True

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))