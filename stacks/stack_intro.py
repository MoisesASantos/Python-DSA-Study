A stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. It only allows items to be added or removed from the top of the stack:

t's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates: it's easy to take an item off the top of the stack, but you can't really get to the items in the middle or at the bottom without removing the items on top first. You'll often hear a stack referred to as a LIFO (last in, first out) data structure.

Whoever decided to take this simple concept and slap a nasty acronym on it should be forced to program in Prolog for the rest of their days.


In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stacks are a great way to implement undo functionality.

For now, we'll just focus on two methods: push and size. Notice that the Stack class already has a constructor and the underlying List that we'll use to store items.

    Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.
    Complete the size method. It should return the number of items in the stack.


Stack Speed

You might be wondering, "why would I use a stack instead of a list?" or "Isn't this just a list with fewer features?"

And you'd be right! A stack is a list with fewer features, but that's the point. By restricting the ways we can interact with the data, we guarantee that certain operations are blazingly fast. Here are all the operations a typical stack supports, along with their Big O time complexity:
Operation 	Big O 	Description
push 	O(1) 	Add an item to the top of the stack
pop 	O(1) 	Remove and return the top item from the stack
peek 	O(1) 	Return the top item from the stack without modifying the stack
size 	O(1) 	Return the number of items in the stack

It's all O(1)! That means no matter how many items are in the stack, these operations will always take the same amount of time. Stacks are really fast and are usually the best choice when the behavior of a stack is all you need.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(len(self.items), item)

    def size(self):
        return len(self.items) 
