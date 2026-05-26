While our avocado toast influencers were happy with our search functionality, now they want to be able to sort all their followers by follower count. Bubble sort is a straightforward sorting algorithm that we can implement quickly, so let's do that!

Complete the bubble_sort function according to the described algorithm above.

def bubble_sort(nums):
    swapping = True
    end = len(nums) - 1
    while swapping:
        swapping = False
        i = 1
        while i <= end:
            if nums[i - 1] > nums[i]:
                j = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = j
                swapping = True
            i += 1
        end -= 1
    return nums
