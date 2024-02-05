def zigzagTraverse(array):
    # O(n * m) time / O(n * m) space; n = height, m = width
    result = []
    isGoingDown = True
    height = len(array) - 1
    width = len(array[0]) - 1
    row = 0
    col = 0
    while row in range(0, height + 1) and col in range(0, width + 1):
        result.append(array[row][col])
        if isGoingDown:
            if col == 0 or row == height:
                isGoingDown = False
                if row == height:
                    col += 1
                elif col == 0:
                    row += 1
            else:
                col -= 1
                row += 1
        else:
            if row == 0 or col == width:
                isGoingDown = True
                if col == width:
                    row += 1
                elif row == 0:
                    col += 1
            else:
                col += 1
                row -= 1

    return result


print(zigzagTraverse([
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]))