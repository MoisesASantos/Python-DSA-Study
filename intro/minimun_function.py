def find_minimum(nums):
    minimun = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if  num < minimun:
            minimun = num
    return minimun
