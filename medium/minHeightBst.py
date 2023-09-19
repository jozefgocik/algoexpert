def minHeightBst(array, tree = None):
    index = len(array) // 2

    if len(array) % 2 == 0:
        index -= 1

    tree = BST(array[index])

    left = array[0:index]
    while len(left) > 0:
        tree.insert(left[len(left) // 2])
        left.pop(len(left)//2)

    right = array[index+1:len(array)]
    while len(right) > 0:
        tree.insert(right[len(right) // 2])
        right.pop(len(right)//2)

    return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# print(minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22]))
print(minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36]))