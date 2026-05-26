We now need a way to show our LockedIn influencers the average (mean) follower count of the people they follow. This will help them know if they're following people who are more or less popular than them.

Complete the average_followers function.

    It should return the average of the given list of numbers.
    If the list is empty, it should return None.

def average_followers(nums):
    if len(nums) == 0:
        return None
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
