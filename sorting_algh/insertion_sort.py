Our influencers want to sort their affiliate deals by revenue. None of our users have more than a couple hundred affiliate deals, so we don't need an n * log(n) algorithm like merge sort. In fact, insertion_sort can be faster than merge_sort, and uses less of our server's memory.

def insertion_sort(nums):

    i = 1
    end = len(nums) - 1
    while i <= end:
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
        i += 1
    return nums
