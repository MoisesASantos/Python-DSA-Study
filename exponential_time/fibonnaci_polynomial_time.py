Our data scientists at LockedIn have found that the growth of the average influencer's follow count is roughly the same growth rate as the Fibonacci sequence! In other words, after 6 weeks of good social media posts, the average influencer will have 8 followers. After 7 weeks, 13 followers, and so on.

The trouble is, our current implementation of the fib function takes so long (exponential time!) to complete that when our influencers navigate to their analytics page it often never completes loading!

Adjust the fib function using the given algorithm to achieve polynomial runtime.

def fib(n):
    if n <= 1:
        return n;
    grandparent = 0
    parent = 1
    current = 0
    for i in range(n - 1):
        current = parent + grandparent

        
        grandparent = parent
        parent = current       
    return current
