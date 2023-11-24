# Solution 1
# def cycleInGraph(edges):
#     # O((v + e) * e) time / O(v) space; v = number of vertices, e = number of edges
#     for i in range(0, len(edges)):
#         if cycleInGraphHelper(edges, i):
#             return True
#
#     return False
#
# def cycleInGraphHelper(edges, ancestor):
#     queue = [ancestor]
#     visited = set()
#     while len(queue) > 0:
#         node = queue.pop(0)
#         if ancestor in edges[node]:
#             return True
#
#         visited.add(node)
#         for i in edges[node]:
#             if i not in visited:
#                 queue.append(i)

# Solution 2
def cycleInGraph(edges):
    # O(v + e) time / O(v) space; v = number of vertices, e = number of edges
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(0, numberOfNodes):
        if visited[node]:
            continue

        containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)
        if containsCycle:
            return True

    return False

def isNodeInCycle(edges, node, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)
            if containsCycle:
                return True

        elif currentlyInStack[neighbor]:
            return True

    currentlyInStack[node] = False
    return False

print(cycleInGraph([
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
]))
