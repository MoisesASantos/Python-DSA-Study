A stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. It only allows items to be added or removed from the top of the stack:

t's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates: it's easy to take an item off the top of the stack, but you can't really get to the items in the middle or at the bottom without removing the items on top first. You'll often hear a stack referred to as a LIFO (last in, first out) data structure.

Whoever decided to take this simple concept and slap a nasty acronym on it should be forced to program in Prolog for the rest of their days.


In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stacks are a great way to implement undo functionality.

For now, we'll just focus on two methods: push and size. Notice that the Stack class already has a constructor and the underlying List that we'll use to store items.

    Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.
    Complete the size method. It should return the number of items in the stack.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(len(self.items), item)

    def size(self):
        return len(self.items) 
