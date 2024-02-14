# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Solution 1
# def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
#     # O(n) time / O(b) space; b = breadth of BST
#     ancestor = -1
#     queue = [nodeTwo]
#     while queue:
#         currentNode = queue.pop(0)
#         if currentNode == nodeOne:
#             ancestor = 1
#             break
#         if currentNode == nodeThree:
#             ancestor = 3
#             break
#         else:
#             if currentNode.left is not None:
#                 queue.append(currentNode.left)
#             if currentNode.right is not None:
#                 queue.append(currentNode.right)
#
#     if ancestor == -1:
#         return False
#
#     queue = [nodeThree if ancestor == 1 else nodeOne]
#     while queue:
#         currentNode = queue.pop(0)
#         if currentNode == nodeTwo:
#             return True
#         else:
#             if currentNode.left is not None:
#                 queue.append(currentNode.left)
#             if currentNode.right is not None:
#                 queue.append(currentNode.right)
#
#     return False

# Solution 2
# def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
#     # O(h) time / O(1) space; h = height of BST
#     if isDescendant(nodeOne, nodeTwo):
#         return isDescendant(nodeTwo, nodeThree)
#
#     if isDescendant(nodeThree, nodeTwo):
#         return isDescendant(nodeTwo, nodeOne)
#
#     return False
#
#
# def isDescendant(ancestor, descendant):
#     while ancestor != descendant and ancestor is not None:
#         ancestor = ancestor.left if ancestor.value >= descendant.value else ancestor.right
#
#     return ancestor == descendant

# Solution 3
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # O(d) time / O(1) space; d = distance between nodeOne and nodeThree
    descendant = None
    searchOne = nodeOne
    searchThree = nodeThree

    while searchOne is not None or searchThree is not None:
        if searchOne == nodeTwo or searchThree == nodeTwo:
            descendant = nodeThree if searchOne == nodeTwo else nodeOne
            break

        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value >= nodeTwo.value else searchOne.right

        if searchThree is not None:
            searchThree = searchThree.left if searchThree.value >= nodeTwo.value else searchThree.right

        if searchOne == searchThree:
            return False


    return isDescendant(nodeTwo, descendant)

def isDescendant(ancestor, descendant):
    while ancestor != descendant and ancestor is not None:
        ancestor = ancestor.left if ancestor.value >= descendant.value else ancestor.right

    return ancestor == descendant
