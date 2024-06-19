# Solution 1
def dijkstrasAlgorithm(start, edges):
    # O(v ^ 2 + e) time / O(v) space; v = number of vertices, e = number of edges
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()

    while len(visited) < numberOfVertices:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)

        if currentMinDistance == float("inf"):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge
            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]

            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance


    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float("inf")
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance

    return vertex, currentMinDistance


print(dijkstrasAlgorithm(
    0,
    [
      [
        [1, 7]
      ],
      [
        [2, 6],
        [3, 20],
        [4, 3]
      ],
      [
        [3, 14]
      ],
      [
        [4, 2]
      ],
      [],
      []
    ]
))