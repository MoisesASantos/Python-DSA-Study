In the current implementation of HashMap, our hashmap has a lot of collisions. This is because we are using a fixed size for our hashmap.

To reduce the chances of a collision, we can increase the number of slots in our hashmap. This is called resizing. This will not eliminate all possible collisions, but it will help reduce the chance of one happening.

When resizing, we create a new hashmap with a larger number of slots. Then, we re-insert all the key-value pairs from the old hashmap into the new hashmap.
Assignment

    Complete the current_load method:
        It returns the number of filled buckets in the hashmap as a ratio of the total number of buckets (In a hashmap, a bucket is simply a slot that stores one or more key-value pairs).
        If the length of the underlying list is zero, return 1.
        Otherwise, divide the number of filled buckets by the length of the underlying list and return it.
    Complete the resize method:
        If the length of the underlying hashmap is 0, make the length 1 (by just adding a None entry) and return.
        Get the current load. If it's less than 5%, do nothing, we have plenty of space
        Otherwise, we need to resize the hashmap.
            Store the current hashmap in a temporary variable
            Create a new empty hashmap that's 10x the size of the current one and assign it to self.hashmap.
            Re-insert all the key-value pairs from the temporary variable into self.hashmap.
    Update the insert method to call resize before inserting a new key-value pair.


from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        self.resize()

        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self) -> None:
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return

        load = self.current_load()

        if load < 0.05:
            return

        old_hashmap = self.hashmap

        new_size = len(old_hashmap) * 10
        self.hashmap = [None for _ in range(new_size)]

        for item in old_hashmap:
            if item is not None:
                key, value = item
                self.insert(key, value)

    def current_load(self) -> float:
        if len(self.hashmap) == 0:
            return 1

        filled = 0

        for bucket in self.hashmap:
            if bucket is not None:
                filled += 1

        return filled / len(self.hashmap)

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
                final += f" - {str(v)}\n"
        return final
