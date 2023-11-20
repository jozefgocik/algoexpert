def cycleInGraph(edges):
    # O((v + e) * e) time / O(v) space; v = number of vertices, e = number of edges
    for i in range(0, len(edges)):
        if cycleInGraphHelper(edges, i):
            return True

    return False

def cycleInGraphHelper(edges, ancestor):
    queue = [ancestor]
    visited = set()
    while len(queue) > 0:
        node = queue.pop(0)
        if ancestor in edges[node]:
            return True

        visited.add(node)
        for i in edges[node]:
            if i not in visited:
                queue.append(i)

print(cycleInGraph([
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
]))
