Implement the recursive delete method. It takes a value as an input and deletes the node with that value if it exists. Each call returns the new root of the tree (or subtree) after the deletion.

Notice that in the test suite the delete method is called like this:

bst = bst.delete(character)

class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None

        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)

            return self

        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)

            return self
        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        successor = self.right

        while successor.left is not None:
            successor = successor.left

        self.val = successor.val

        self.right = self.right.delete(successor.val)

        return self
            

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

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
