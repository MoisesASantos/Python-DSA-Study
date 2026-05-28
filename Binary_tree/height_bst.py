

Complete the height method. It returns the height of the tree rooted at the current node.

    If the node's value is None, return 0.
    Recursively calculate the height of the left subtree.
    Recursively calculate the height of the right subtree.
    Use the max() function to return the maximum of the left and right subtree heights plus 1.

class BSTNode:
    def height(self):
        if self.val is None:
            return 0

        left_height = 0
        right_height = 0

        if self.left is not None:
            left_height = self.left.height()

        if self.right is not None:
            right_height = self.right.height()

        return 1 + max(left_height, right_height)

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
