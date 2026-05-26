Complete the decayed_followers function.

It calculates the final value of a quantity after a certain time has passed, given its initial value and a rate of decay. Return the remaining followers.

remaining_total = quantity * ( retention_rate ^ time )

The retention_rate is the opposite of fraction_lost_daily. If an influencer lost 0.2 (or 20%) of their followers each day, then the retention rate would be 0.8 (or 80%).
Example

With these parameters:

    initial_followers = 100
    fraction_lost_daily = 0.5

Then we expect these results:

    After 0 days: 100 followers
    After 1 day: 50 followers
    After 2 days: 25 followers
    After 3 days: 12.5 followers (rounded down)


def decayed_followers(initial_followers, fraction_lost_daily, days):
    retantion_rate = initial_followers - fraction_lost_daily
    return initial_followers * (retantion_rate ** days)
