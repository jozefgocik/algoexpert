# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def repairBst(tree):
    # O(n) time / O(h) space; h = height of BST
    nodeOne = nodeTwo = previous = None

    def repairBstHelper(node):
        nonlocal nodeOne, nodeTwo, previous

        if node is None:
            return

        repairBstHelper(node.left)

        if previous is not None and node.value < previous.value:
            if nodeOne is None:
                nodeOne = previous
            nodeTwo = node
        previous = node

        repairBstHelper(node.right)

    repairBstHelper(tree)

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree

