To use our Linked List as a fast queue (O(1) pushes and pops) we need our add_to_tail function to be O(1). Currently, it iterates over the entire list before appending an item. We can fix this by keeping track of the last item with a new data member: tail.

Note: It's common in algorithms to make this kind of trade-off. By using a little extra memory (keeping track of tail), we can make our operations faster. Sometimes you might need to go the other way, and use more computation time to save memory.
Assignment

LockedIn's queue was working just fine on small datasets, but appending items once the list has 100,000+ items has started to take a toll on our servers. Implement these changes to speed up our Linked List's inserts to O(1):

    Update the constructor to set self.tail to None.
    Update add_to_head to also set the tail reference to the given node if the list is empty.
    Update add_to_tail:
        Set the head and tail to the given node if the list is empty.
        Instead of iterating through the list to find the last node, use the tail node to append the new node (for example, set self.tail.next to the new node).
        Update the tail reference to new node.

from node import Node


class LinkedList:
    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None
        

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
