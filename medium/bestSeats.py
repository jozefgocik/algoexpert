def bestSeat(seats):
    # O(n) time / O(1) space
    intervalLength = -1
    index = -1

    i = 1
    while i < len(seats) - 1:
        if seats[i] == 0:
            interval = [i, i]

            while seats[i] == 0:
                i += 1
                if seats[i] == 0:
                    interval[1] += 1

            if interval[1] - interval[0] > intervalLength:
                intervalLength = interval[1] - interval[0]
                index = sum(interval)//2
        else:
            i += 1

    return index

print(bestSeat([1, 0, 1, 0, 0, 0, 1]))
# 4
print(bestSeat([1, 0, 0, 1]))
# 1
print(bestSeat([1, 0, 0, 1, 0, 0, 1]))
# 1