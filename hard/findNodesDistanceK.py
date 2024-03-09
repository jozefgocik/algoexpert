# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution 1
# def findNodesDistanceK(tree, target, k):
#     # O(n) time / O(n) space
#     result = []
#     parents = {}
#     findParents(tree, None, parents)
#     targetNode = getNodeFromValue(tree, target, parents)
#
#     visited = set()
#     queue = [(targetNode, 0)]
#     while queue:
#         current = queue.pop(0)
#         node = current[0]
#         distance = current[1]
#
#         if distance == k and node.value not in visited:
#             result.append(node.value)
#         visited.add(node.value)
#
#         if node.left is not None and node.left.value not in visited:
#             queue.append((node.left, distance + 1))
#         if node.right is not None and node.right.value not in visited:
#             queue.append((node.right, distance + 1))
#         if parents[node.value] is not None and parents[node.value] not in visited:
#             queue.append((parents[node.value], distance + 1))
#
#     return result
#
#
# def getNodeFromValue(tree, value, parents):
#     if tree.value == value:
#         return tree
#
#     nodeParent = parents[value]
#     if nodeParent.left and nodeParent.left.value == value:
#         return nodeParent.left
#
#     return nodeParent.right
#
#
# def findParents(tree, parent, parents):
#     if tree is None:
#         return
#
#     parents[tree.value] = parent
#     parent = tree
#
#     findParents(tree.left, parent, parents)
#     findParents(tree.right, parent, parents)

# Solution 2
def findNodesDistanceK(tree, target, k):
    # O(n) time / O(n) space
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)

    return bfsForNodesDistanceK(targetNode, nodesToParents, k)


def bfsForNodesDistanceK(targetNode, nodesToParents, k):
    queue = [(targetNode, 0)]
    visited = {targetNode.value}

    while queue:
        currentNode, distanceFromTarget = queue.pop(0)

        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK

        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in visited:
                continue

            visited.add(node.value)
            queue.append((node, distanceFromTarget + 1))

    return []

def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree

    nodeParent = nodesToParents[value]
    if nodeParent.left and nodeParent.left.value == value:
        return nodeParent.left

    return nodeParent.right


def populateNodesToParents(tree, nodesToParents, parent = None):
    if tree:
        nodesToParents[tree.value] = parent
        populateNodesToParents(tree.left, nodesToParents, tree)
        populateNodesToParents(tree.right, nodesToParents, tree)
