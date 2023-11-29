def twoColorable(edges):
    # O(v + e) time / O(v) space; v = number of vertices, e = number of edges
    # True = Color1, False = Color2
    colors = [None for _ in range(0, len(edges))]
    colors[0] = True

    stack = [0]
    while len(stack) > 0:
        node = stack.pop()
        for connection in edges[node]:
            if colors[connection] is None:
                colors[connection] = not colors[node]
                stack.append(connection)
            elif colors[connection] == colors[node]:
                return False

    return True

print(twoColorable([
  [1],
  [0]
]))
print(twoColorable([
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]))