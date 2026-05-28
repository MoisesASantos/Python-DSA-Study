Let's use our Trie to find the longest common prefix of a list of words. This feature can be used in LockedIn to display suggestions when users are searching for their connections.
Assignment

Complete the longest_common_prefix method. It returns the longest common prefix among the words in the trie.

    Initialize a variable current that references the root of the trie
    Initialize a variable prefix to an empty string
    Enter a forever while loop:
        Get the "children" (keys) list by iterating over the keys of current dictionary.
            If a "child" (key) is an end_symbol, break the inner loop. Otherwise, append to the list.
        If there is only one child, append the character to the prefix string and update the current dictionary to point to the child dictionary corresponding to the character.
        If there are multiple children or no children, break the loop.
    Return the prefix string.

from typing import Any


class Trie:
    def longest_common_prefix(self) -> str:
        current = self.root
        prefix = ""

        while True:
            children = []

            for key in current.keys():
                if key == self.end_symbol:
                    continue
                children.append(key)

            if len(children) != 1:
                break

            char = children[0]
            prefix += char
            current = current[char]

        return prefix

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
