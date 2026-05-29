Assignment

The LockedIn influencers are worried about account security. We've assured them that their passwords are secure enough, but they want data. Assuming a brute-force guessing strategy on the part of an attacker, we want to know the maximum number of passwords they would have to try.

Complete the get_num_guesses function. It takes a password length as input and returns the number of all possible passwords of that length and shorter. Only the 26 lowercase English letters can be used in these passwords for the sake of simplicity.

For example, here's the math for calculating the total number of possible passwords for a password length of 3:

26 + 26^2 + 26^3 = 18278

More examples:
Password Length 	Num of Possibilities
1 	26
2 	702
3 	18278

def get_num_guesses(length: int) -> int:
    num_comb = 0
    for i in range(1, length + 1):
        num_comb += 26 ** i

    return num_comb
