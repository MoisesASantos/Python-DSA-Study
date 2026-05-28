As it turns out, the binary search tree was overkill for profile lookups on the LockedIn website. We don't need any of the fancy ordered traversals or range queries after all - and because LockedIn is such a business failure (our CEO's words, not mine) we can store every user in memory, no need to save them to the hard drive.

Let's build a hashmap! We'll use the strings (usernames) as keys, and map them to user objects.

Complete the HashMap's key_to_index method. It should:

    Take a key (string) as input
    Calculate the sum of the Unicode values of all the characters in the string using Python's ord function
    Mod (%) the sum by the length of the hashmap (which is built on top of a list) to get an index which should be an int
    Return the index

from typing import Any


class HashMap:
    def key_to_index(self, key: str) -> int:
        sum_uni = 0
        for char in key:
            sum_uni += ord(char)
        result = sum_uni % len(self.hashmap)
        return result

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def __repr__(self) -> str:
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
