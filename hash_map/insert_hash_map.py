Insert

Now that we have some building blocks for our hashmap, we need a way to start inserting values.
Assignment

Complete the insert method. It accepts a string key and an associated value (in this case, LockedIn user records).

    Convert the incoming key to the appropriate storage index using your existing hash function
    Create a key-value pair as a tuple
    Store the tuple at the calculated index in the underlying array

The resulting structure should look something like this, with key-value pairs at some positions and empty slots at others:

[
    (key, val),
    None,
    None,
    (key, val),
    None,
    ...
]

Indexes with an entry will contain a tuple, and empty indexes will contain the None value.

from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        new_index = self.key_to_index(key)
        key_value = (key, value)
        self.hashmap[new_index] = key_value
    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final
