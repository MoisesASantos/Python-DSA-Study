Let's solve a commonly misunderstood problem in computer science - finding the prime factors of a number. Almost all modern cryptography, including your browser's HTTPS encryption, is based on the fact that prime factorization is slow.

For now, let's focus on the speed of factorization, and how it relates to P and NP.

Finding a number's prime factors is an NP algorithm.

    When given two primes and their product, all we need to do is some simple multiplication to verify correctness. (polynomial time)
    Given a number, finding its prime factors is a much more difficult problem. Exponential time is the best we know of.

The trouble is that no one has formally proven that there is not a polynomial time algorithm for finding prime factors. So, we're technically unsure if the problem is in P or if it's NP-complete.

Either way, let's build it!
The Algorithm

Given a large number, return a list of all the prime factors.

    prime_factors(8) -> [2, 2, 2]
    prime_factors(10) -> [2, 5]
    prime_factors(24) -> [2, 2, 2, 3]

    Divide n by 2 as many times as you can evenly (no remainder). For each division, append a 2 to the list of prime factors.
    By now, n must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of n inclusive. Use math.sqrt(). For each number i:
        If n can be divided evenly by i, then divide n by i and append i to the list.
        Repeat this (nested loop) until n cannot be divided evenly by i, then move on to the next i.
    If n is still greater than 2 after that loop, it must still be prime, so just append it to the list.
    Return the list of primes, ordered from least to greatest.

Assignment

Complete the prime_factors function according to the given algorithm. Notice how the algorithm gets much slower as the size of the input (in bits) grows.

The returned list should only contain ints, no floats.

import math

def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors
