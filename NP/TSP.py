Assignment

Our influencers need to travel to conferences to shill their sponsor's products! Since none of them trust Google Maps, they want to put in their proposed route to LockedIn, and we will tell them if their route is short enough to be worth their time (can you say feature creep?).

Complete the tsp function by performing a brute-force search using the provided algorithm. The brute-force search will, unfortunately, take factorial time, O(n!), because you will need to try all possible paths and keep track of the shortest.

The provided permutations() will give you all the possible permutations of a list. For example, permutations([0,1,2]) returns:

[
  [0, 1, 2],
  [0, 2, 1],
  [1, 0, 2],
  [1, 2, 0],
  [2, 0, 1],
  [2, 1, 0]
]

Pseudocode

Inputs:

    cities: A list of numbers starting from 0 that each represent a city.
    paths: A matrix where each point represents the distance between two cities.
    dist: The distance we are trying to beat.

Here's an example of the paths matrix (a list of lists). Each list represents the distance from that city to all the other cities. For example, paths[0][1] holds the distance from city 0 to city 1. paths[0][1] = paths[1][0]

paths = [
    [0, 12, 30], # list 0 shows the distance from city 0 to cities 0, 1 and 2
    [12, 0, 15], # list 1 shows the distance from city 1 to cities 0, 1 and 2
    [30, 15, 0], # list 2 shows the distance from city 2 to cities 0, 1 and 2
]

# all of the routes and their distances:

paths[0][1] # 12
paths[0][2] # 30
paths[1][2] # 15

# the shortest distance between all cities is from city 0 to city 1 to city 2, which is 27

Algorithm:

    Use the permutations function to get the matrix of all possible paths through the given cities. Where the first path, [0, 1, 2] represents moving from city 0 -> city 1 -> city 2
    Iterate over each possible path (permutation)
        Sum the distances between each city in the path using the paths matrix to look up the distances
        If the total distance of the path is less than the given dist return True
    If no short paths were found, return False

You'll want to use a nested loop here! An outer loop over all permutations (paths), and an inner loop to sum the distances of consecutive city pairs within a single path

def tsp(cities: list[str], paths: list[list[int]], dist: int) -> bool:
    permut = permutations(cities)

    for path in permut:
        total_distance = 0

        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]

            total_distance += paths[city1][city2]

        if total_distance < dist:
            return True

    return False
