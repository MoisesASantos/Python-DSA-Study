We have a popular influencer using our LockedIn app, and she needs to be able to quickly search for posts from a particular day. This function will be the backbone of her search screen.

Complete the binary_search function. It should follow the algorithm as described above.

def binary_search(target, arr):
    new_list = sorted(arr)
    low = 0
    high = len(new_list) - 1
    while low <= high:
        median_value = (low + high) // 2
        if new_list[median_value] == target:
            return True
        elif new_list[median_value] < target:
            low = median_value + 1
        else:
            high = median_value - 1
    return False
