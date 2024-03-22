def knapsackProblem(items, capacity):
    # O(n ^ 2) time / O(n ^ 2) space
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    values = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(values)):
        for j in range(1, len(values[i])):
            item = items[i - 1]
            value = item[0]
            weight = item[1]
            if weight <= j:
                values[i][j] = max(values[i - 1][j], value + values[i - 1][j - weight])
            else:
                values[i][j] = values[i - 1][j]

    indices = []
    i = len(items)
    j = capacity
    while i > 0 and j > 0:
        if values[i][j] == values[i - 1][j]:
            i -= 1
        else:
            indices.append(i - 1)
            j -= items[i - 1][1]
            i -= 1

    return [values[-1][-1], indices]


print(knapsackProblem([
  [1, 2],
  [4, 3],
  [5, 6],
  [6, 7]
], 10))