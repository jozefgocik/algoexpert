def taskAssignment(k, tasks):
    # O(n * log(n)) time / O(n) space
    pairedTasks = []

    sortedTasks = sorted(tasks)
    indices = {}
    for i in range(0, len(tasks)):
        if tasks[i] not in indices:
            indices[tasks[i]] = []
        indices[tasks[i]].append(i)

    for i in range(0, k):
        a = indices[sortedTasks[i]].pop()
        b = indices[sortedTasks[len(tasks) - 1 - i]].pop()
        pairedTasks.append([a, b])

    return pairedTasks

print(taskAssignment(3, [1, 3, 5, 3, 1, 4]))