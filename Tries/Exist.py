In a trie, "hello", "help" and "hi" would be represented as:

{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}

Assignment

We want to be able to see what words have been added to the trie.

Complete the exists method. It takes a word as input, and should return True if the word exists in the trie, and False if it doesn't.

    Starting with the root of the trie, assign the current dictionary to a variable.
    Loop over the letters in the word.
        If the current letter is not in the current dictionary, return False.
        Update current to point to the dictionary at the letter key.
    Once you get to the last letter, return True if end_symbol is in the current dictionary, and False if it isn't.

from typing import Any


class Trie:
    def exists(self, word: str) -> bool:
        current_level = self.root
        for char in word:
            if char not in current_level:
                return False
            current_level = current_level[char]
        return self.end_symbol in current_level

    # don't touch below this line

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"
