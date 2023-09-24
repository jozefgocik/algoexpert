# Solution 1
# def invertBinaryTree(tree):
#     # O(n) time / O(h) space; h = BT height
#     if tree is None:
#         return
#
#     tree.left, tree.right = tree.right, tree.left
#     invertBinaryTree(tree.left)
#     invertBinaryTree(tree.right)
#
#     return tree

# Solution 2
def invertBinaryTree(tree):
    # O(n) time / O(n) space
    queue = [tree]

    while len(queue) > 0:
        currentTree = queue.pop(0)
        if currentTree is None:
            continue
        else:
            currentTree.left, currentTree.right = currentTree.right, currentTree.left
            queue.append(currentTree.left)
            queue.append(currentTree.right)

    return tree

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None