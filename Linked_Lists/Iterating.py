Even though iterating with linked lists kinda sucks compared to the simplicity of arrays (normal lists), we've got to do it. Although the implementation is more complex and slow, we can still make it easy for users of our class by providing an __iter__ method.
The yield Keyword

The yield keyword in Python returns a value, kind of like return. However, it's used to turn the function into a generator function.

A generator function creates a new function object. When that function is called, it executes the code in the generator function until it hits a yield statement. At that point, the function pauses and returns the value of the yield statement. The next time the function is called, it picks up right where it left off.

def create_message_generator():
    yield "hi"
    yield "there"
    yield "friend"

gen = create_message_generator()
first = next(gen)
print(first)  # prints: hi
second = next(gen)
print(second)  # prints: there
third = next(gen)
print(third)  # prints: friend

Every time you call create_message_generator(), it creates a new generator instance. To continue from where you left off, you need to assign this generator to a variable (like gen in the example above). This way, when you use next() or loop over the generator, you're continuing with the same instance rather than starting a new one.
Assignment

The LinkedList class is a wrapper class that uses the Node class we already wrote.

    Complete the __init__ method. It should set the head field to None.

No other node points to the linked list's head (first) node, so the LinkedList class itself needs to keep track of it. We'll use the term head and tail like this:

head node -> node -> node -> node -> tail node

The direction of flow above might feel opposite to what you're used to with a Queue, but it's really the same. Above I'm using arrows to show which nodes are pointing to which other nodes. In a future lesson when we implement a Queue using a LinkedList, we'll add elements to the tail and remove elements from the head.

    Complete the __iter__ method. It should be a generator function that yields each node in the linked list, from the head to the tail.
        Create a reference to the head node (e.g. node = self.head)
        Use a while loop to iterate over the linked list until node is None
            Yield the current node
            Set node to the next node

We need to change which node is the next to be yielded, but the set_next method of the Node class changes which is the next to be pointed to – don't use it!

By overriding the __iter__ method, Python will allow us to use a for loop to iterate over the linked list:

from node import Node

ll = LinkedList()
ll.head = Node("first")
ll.head.next = Node("second")
ll.head.next.next = Node("third")

for node in ll:
    print(node.val)

from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
