While the influencers who use our platform are really great at taking selfies, most aren't super great at math. We need to write a tool that predicts an influencer's follower growth over time.

Complete the get_follower_prediction function. It takes a follower_count integer, an influencer_type string and a num_months integer, and returns an integer.

Calculate the number of followers an influencer will have after a given number of months according to the influencer type:

    "fitness": follower count quadruples each month
    "cosmetic": follower count triples each month
    other: follower count doubles each month

For example, if a "fitness" influencer starts with 10 followers, then after 1 month they would have 40 followers. After 2 months, they would have 160 followers, and so on.

This kind of sequence, where each term is found by multiplying the previous term by a constant, is called a geometric sequence or geometric progression.

Use the following version of the geometric progression formula, in which a1 is the initial number of followers, r is the multiplication constant, and n is the number of months:

total = a1 × r^n

def get_follower_prediction(follower_count, influencer_type, num_months):
    if  influencer_type == "fitness":
        i = 0
        follower_growth = follower_count
        while i < num_months:
            follower_growth *= 4
            i += 1
    elif influencer_type == "cosmetic":
        i = 0
        follower_growth = follower_count
        while i < num_months:
            follower_growth *= 3
            i += 1
    else:
        i = 0
        follower_growth = follower_count
        while i < num_months:
            follower_growth *= 2
            i += 1
    return follower_growth

Note: At this moment my code should be better, but I have few time to complete the lesson so I just make to work, late, I'll review this and make something better


And 2 minutes later, I decide to make the better code now, and, lady's and gentleman

def get_follower_prediction(follower_count, influencer_type, num_months):
    if  influencer_type == "fitness":
            follower_growth = follower_count * 4 ** num_months
    elif influencer_type == "cosmetic":
            follower_growth = follower_count * 3 ** num_months
    else:
            follower_growth = follower_count * 2 ** num_months
    return follower_growth


