Complete the exists method.

It should take a value as input and return True if the value exists in the tree, and False if it doesn't. It's a recursive method, as you probably guessed.

class BSTNode:
    def exists(self, val):
        if self.val == val:
            return True

        if val < self.val:
            if self.left is None:
                return False

            return self.left.exists(val)

        else:
            if self.right is None:
                return False

            return self.right.exists(val)
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
