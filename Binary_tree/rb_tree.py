As it turns out, we've been inserting user records into our tree with incrementing numerical IDs (pre sorted data)! The app's user lookups are starting to get really slow. Let's start implementing a Red-Black tree to speed things up.

In a normal BST, the child nodes don't need to know about, or carry a reference to their parent. The same is not true for Red-Black trees.

The RBNode class is already implemented for you, as well as the __init__ constructor method of the RBTree class. There's also a data member, self.nil created for you in the constructor. self.nil contains the value we'll use to designate all the nil (empty) leaf nodes, which are used for rebalancing purposes but contain no "actual" value.

Complete the insert method. It should take a value as input and add the value as a new node in the tree if the value doesn't already exist.

from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)

        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root

        while current != self.nil:
            parent = current

            if new_node.val < current.val:
                current = current.left

            elif new_node.val > current.val:
                current = current.right

            else:
                return

        new_node.parent = parent

        if parent is None:
            self.root = new_node

        elif new_node.val < parent.val:
            parent.left = new_node

        else:
            parent.right = new_node
