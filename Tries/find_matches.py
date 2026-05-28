Find Matches

Tries are super efficient when it comes to finding substrings in a large document of text. For LockedIn, we want to be able to find all of the instances of bad words in chat messages and filter them out.

If we just split on whitespace and matched against a dictionary, we would miss substrings. For example, if we had the word "darn" in our dictionary, we would allow the word "darnit" to slip through undetected. That's why we'll use a trie.
Assignment

Complete the find_matches method. It takes an entire document string as input and returns a set() of all the words from the trie that occur in the document.

    Create a new set() to store the matches.
    Loop over all the indexes of the characters in the document (this value marks the start of the substring).
        Keep track of your current level in the trie (a dictionary) starting at the root.
        Use another nested loop to iterate over all the indexes of characters in the document, but start at the current index of the outer loop. (this value marks the potential end of the substring)
            If the inner character is not in the current level, break out of the inner loop, there are no matches here.
            Otherwise, move to the next level in the trie (based on the inner character).
            If the inner character's level contains the end symbol, add the substring to the matches set. You can calculate the full substring by slicing the document using the indexes of the outer and inner loops.
    Return the set of matches.

from typing import Any


class Trie:
    def find_matches(self, document: str) -> set[str]:
        matches = set()

        for i in range(len(document)):
            current_level = self.root

            for j in range(i, len(document)):
                char = document[j]

                if char not in current_level:
                    break

                current_level = current_level[char]

                if self.end_symbol in current_level:
                    matches.add(document[i:j + 1])

        return matches

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
