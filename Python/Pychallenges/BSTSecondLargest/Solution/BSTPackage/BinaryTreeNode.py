class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def subtree(self, nodeleft, noderight):
        self.left = nodeleft
        self.right = noderight