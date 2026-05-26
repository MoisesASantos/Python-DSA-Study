Our LockedIn influencers are complaining that when they sort their followers by follower count, it gets really slow if they have more than 1,000 followers (because we're using Bubble Sort). Let's speed it up for them with merge sort.

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2

    merge_left = nums[:mid]
    merge_right = nums[mid:]

    sorted_left = merge_sort(merge_left)
    sorted_right = merge_sort(merge_right)
    
    return merge(sorted_right, sorted_left)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
