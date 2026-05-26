When you run your completed code, notice how each successive call to does_name_exist takes quite a bit longer. Assuming the length of first_names and last_names is the same, each new name doesn't add n steps to the algorithm; the total number of steps grows quadratically with the size of the input, making the total work O(n^2).

If does_name_exist(10 names, 10 names) takes just 1 second to complete, then we can estimate:

    does_name_exist(100 names, 100 names) = 100 seconds
    does_name_exist(1000 names, 1000 names) = 10,000 seconds
    does_name_exist(10000 names, 10000 names) = 1,000,000 seconds


def does_name_exist(first_names, last_names, full_name):
    for f_name in first_names:
        for l_name in last_names:
            if (f_name + " " + l_name) == full_name:
                return True
    return False
