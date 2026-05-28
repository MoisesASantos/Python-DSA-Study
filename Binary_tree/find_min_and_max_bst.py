Now that we can add users to our BST, our systems team wants us to start implementing search functionality.

Implement the get_min and get_max methods. They should return the minimum and maximum values in the BST respectively.

class BSTNode:
    def get_min(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.val

    def get_max(self):
        node = self
        while node.right is not None:
            node = node.right
        return node.val

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
