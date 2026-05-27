Now that we can add items to our stack, we need to be able to view the top item, and remove the top item.
Assignment

    Complete the peek method. It should return the top item from the stack without modifying the stack. If the stack is empty, return None.
    Complete the pop method. It should remove and return the top item from the stack. If the stack is empty, return None.

All supported operations are O(1) by themselves. However, some tasks, like getting to an item at the bottom of the stack have a higher time complexity because they require multiple pop operations.
Stack operations are limited: no searching, no sorting, no random access
Stacks, like all abstract data types, can store items of any type. What makes it a stack is the behavior of the operations, not the type of data it stores.
Stacks are often used in the real world for:

    Function call management
    Undo/redo functionality
    Expression evaluation
    Browser history



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp
