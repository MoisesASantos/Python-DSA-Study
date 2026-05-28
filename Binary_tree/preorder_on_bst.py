Implement the recursive preorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.

For example, the first call to preorder on an entire tree would be:

# an empty list is passed in the first call
bst_node.preorder([])

class BSTNode:
    def preorder(self, visited):
        node = self

        if node.val is not None:
            visited.append(node.val)
            if node.left is not None:
                node.left.preorder(visited)
            if node.right is not None:
                node.right.preorder(visited)
        return visited
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
