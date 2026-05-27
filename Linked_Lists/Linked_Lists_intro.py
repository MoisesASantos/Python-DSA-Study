Remember how the push method on our Queue is O(n) instead of O(1)?

def push(self, item):
    # everything in self.items has to shift
    # up a position, which takes O(n) time
    self.items.insert(0, item)

Let's fix that.

To build a faster queue, we'll use a Linked List instead of a regular List (array) under the hood. A linked list is where elements are not stored next to each other in memory, instead, each item references the next in a chain.

Nodes

Our nodes will be represented by a simple class with two fields:

    val - The raw string value that the node holds (e.g. 'Carla', 'James', etc)
    next - A reference to the next node in the list

Assignment

Let's lock-in and make LockedIn faster!

    Complete the Node's constructor.
        Set its val field to the provided value.
        Set its next field to None.
    Complete the Node's set_next method. It should set the next field to the provided node.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
