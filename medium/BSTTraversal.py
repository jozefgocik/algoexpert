def inOrderTraverse(tree, array):
    # O(n) time / O(n) space
    if tree is None:
        return

    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)

    return array

def preOrderTraverse(tree, array):
    # O(n) time / O(n) space
    if tree is None:
        return

    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)

    return array

def postOrderTraverse(tree, array):
    # O(n) time / O(n) space
    if tree is None:
        return

    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)

    return array

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.right = BST(22)

inOrder = [1, 2, 5, 5, 10, 15, 22]
preOrder = [10, 5, 2, 1, 5, 15, 22]
postOrder = [1, 2, 5, 5, 22, 15, 10]

print(inOrderTraverse(root, []))
print(preOrderTraverse(root, []))
print(postOrderTraverse(root, []))
