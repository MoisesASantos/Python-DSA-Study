Complete the add_to_tail method. It adds a new node to the end of the list and returns nothing.

    If there isn't a head node, set the new node as the head and return.
    Otherwise, keep a reference to the "last" node in the list - start with it set to the head.
    Iterate over the linked list (you can use a for loop now that you've added your own __iter__!)
        Update your "last" node reference to the current node
    Once you've iterated over the entire list, your "last" reference should be the last node in the list (the "tail"). Set the next field of the "last" node to the new node.

from node import Node


class LinkedList:
    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return 
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = node
        

    # don't touch below this line

    def __init__(self):
        self.head = None

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
