def diskStacking(disks):
    # O(n ^ 2) time / O(n) space
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for _ in disks]
    maxHeightIdx = 0

    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if canStack(currentDisk, otherDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j

        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i

    return buildSequence(disks, sequences, maxHeightIdx)


def buildSequence(disks, sequences, index):
    sequence = []
    while index is not None:
        sequence.append(disks[index])
        index = sequences[index]

    return sequence[::-1]


def canStack(bottom, top):
    return bottom[0] > top[0] and bottom[1] > top[1] and bottom[2] > top[2]


print(diskStacking([
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]
]))
