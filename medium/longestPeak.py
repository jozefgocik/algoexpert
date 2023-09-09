def longestPeak(array):
    # O(n) time / O(1) space
    peakIndexes = []
    for i in range(1, len(array) - 1):
        a = array[i - 1]
        b = array[i]
        c = array[i + 1]

        if a < b > c:
            peakIndexes.append(i)

    length = 0
    for index in peakIndexes:
        currentLength = 0
        for i in range(0, index)[::-1]:
            if array[i] > array[i - 1]:
                currentLength += 1
            else:
                currentLength += 1
                break

        for j in range(index, len(array)):
            if j + 1 < len(array) and array[j] > array[j + 1]:
                currentLength += 1
            else:
                currentLength += 1
                break

        if currentLength > length:
            length = currentLength

    return length

print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
# 6 => 0, 10, 6, 5, -1, -3
