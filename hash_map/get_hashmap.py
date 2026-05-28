


Assignment

Complete the get method. It takes a key (a string) and returns the value stored at that location (not the whole key/value tuple).

Use the key_to_index method to find the correct index to look up in the self.hashmap datastore, and if a value doesn't exist at that index, raise the following Exception to indicate no key was found.

raise Exception("sorry, key not found")

Due to our simple implementation, some of the keys that are inserted into the hashmap will have colliding values, which may lead to strange results - that's okay!


from typing import Any


class HashMap:
    def get(self, key: str) -> Any:
        index_value = self.key_to_index(key)
        item = self.hashmap[index_value]
        if item is None:
           raise Exception("sorry, key not found") 
        stored_key, stored_value = item
        if stored_key == key:
            return stored_value

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def insert(self, key: str, value: Any) -> None:
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
