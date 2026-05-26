LockedIn users want to know which of their followers has the highest engagement score.

Complete the find_max function. It should take a list of integers and return the largest value in the list.

The "runtime complexity" (aka Big O) of this function should be O(n).


def find_max(nums):
    max_value = float('-inf')
    for num in nums:
        if num > max_value:
            max_value = num

    return max_value
