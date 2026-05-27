Write a function log_scale(data, base) that takes a list of positive numbers data, and a logarithmic base, and returns a new list with the logarithm of each number in the original list, using the given base.

You may want to use the math.log() function.

Example:

log_scale([1, 10, 100, 1000], 10)
# Output: [0.0, 1.0, 2.0, 3.0]

log_scale([1, 2, 4, 8], 2)
# Output: [0.0, 1.0, 2.0, 3.0]


import math

def log_scale(data, base):
    list_new = list()
    for i in data:
        list_new.append(math.log(i, base))
    return list_new
