def runLengthEncoding(string):
    # Write your code here.
    result = ""
    currentLength = 1
    for i in range(1, len(string)):
        currentChar = string[i]
        previousChar = string[i - 1]

        if currentChar != previousChar or currentLength == 9:
            result += (str(currentLength) + previousChar)
            currentLength = 0

        currentLength += 1

    result += (str(currentLength) + previousChar)

    return result

runLengthEncoding("AAAAAAAAAAAAABBCCCCDD") #9A4A2B4C2D
