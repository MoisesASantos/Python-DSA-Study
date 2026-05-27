Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day.

def exponential_growth(n, factor, days):
    exponential_grow = list()
    for i in range(days + 1):
        exponential_grow.append(n)
        n *= factor
    return exponential_grow
