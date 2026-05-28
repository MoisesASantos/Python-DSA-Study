Tries

Tries are one of my favorite data structures, I've used them often in the past for natural language processing tasks. In Python, a trie is easily implemented as a nested tree of dictionaries where each key is a character that maps to the next character in a word. For example, the words:

    hello
    help
    hi

Would be represented as:

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

The * character (paired with True instead of a dictionary) is used to indicate the end of a word.

A trie is also often referred to as a "prefix tree" because it can be used to efficiently find all of the words that start with a given prefix.

Try building the example trie:
Trie Builder
Build a trie one character at a time from shared word prefixes.
Wordhi
Current hi
Complete 2
h
e
l
l
o
*
p
*
i
14 / 15
Current step
Create the i node for prefix hi.
Assignment

We're going to use a trie to add "prefix searching" to LockedIn. For example, a user will be able to type "dev" into a job search bar and see the autocomplete suggestions "developer", "development", "devops", etc.

Complete the add method. It takes a word as input, and should add it to the trie.

    Keep track of your "current level" in the trie, starting at the root.
    Loop over each character in the word-to-add:
        If the character is not a key in the current level, add it and create a new nested level (dictionary) for it.
        Outside the if statement, update your "current level" to the nested dictionary for this character (whether it was just created or already existed).
    Once you've ensured all the dictionaries exist, add an entry to the dictionary of the last character in the word with self.end_symbol as the key and True as the value. This will indicate that this is a complete word and not just a prefix of another word.

from typing import Any


class Trie:
    def add(self, word: str) -> None:

        current_level = self.root

        for char in word:
            if char not in current_level:
                current_level[char] = {}

            current_level = current_level[char]

        current_level[self.end_symbol] = True   

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"
