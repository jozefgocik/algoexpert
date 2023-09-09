# Solution 1
def mergeOverlappingIntervals(intervals):
    # O(nLog(n)) time / O(n) space
    intervals.sort()
    result = []

    i = 0
    while i < len(intervals):
        currentInterval = intervals[i]
        j = i + 1
        while j < len(intervals):
            if currentInterval[0] <= intervals[j][0] and currentInterval[1] >= intervals[j][1]:
                i += 1
                j += 1
            elif currentInterval[1] >= intervals[j][0]:
                currentInterval[1] = intervals[j][1]
                i += 1
                j += 1
            else:
                break

        result.append(currentInterval)
        i += 1

    return result

print(mergeOverlappingIntervals([
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]))
# [[1, 2], [3, 8], [9, 10]]
print(mergeOverlappingIntervals([
    [-20, 30],
    [1, 22],
]))
# [-20, 30]
print(mergeOverlappingIntervals([
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [1, 10]
]))
# [1, 10]