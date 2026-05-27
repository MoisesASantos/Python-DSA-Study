Assignment

LockedIn uses a Queue to keep track of the order that recruiters should use to reach out to job seekers.

Implement the following operations on the Queue class:

    queue.push(item): Adds an item to the tail of the queue (index 0 of list)
    queue.pop(): Removes and returns an item from the head of the queue (last index of list)
    queue.peek(): Returns an item from the head of the queue
    queue.size(): Returns the number of items in the queue

Note: You'll often hear words used interchangeably in programming. For example, here we're saying push and pop, but enqueue and dequeue are also common words for the same ideas.
term 1 	term 2 	description
Push 	Enqueue 	Adds an item to the tail of the queue
Pop 	Dequeue 	Removes and returns an item from the head of the queue


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[0]
        del self.items[0]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)
