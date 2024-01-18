def reverseWordsInString(string):
    # O(n) time / O(n) space
    result = []

    currentWord = ""
    for i in range(len(string)):
        if string[i] == " ":
            result.append(currentWord)
            result.append(" ")
            currentWord = ""
        else:
            currentWord += string[i]

    result.append(currentWord)
    reverseList(result)

    return "".join(result)

def reverseList(listToReverse):
    left = 0
    right = len(listToReverse) - 1
    while left < right:
        listToReverse[left], listToReverse[right] = listToReverse[right], listToReverse[left]
        left += 1
        right -= 1


print(reverseWordsInString("AlgoExpert is the best!"))