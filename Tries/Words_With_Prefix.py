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

Complete the search_level function. This recursive function collects all complete words starting from the current trie level. It takes the current dictionary level, the accumulated prefix string, and the list of words found.

    Check for complete words:
        If the current level contains an end marker, add the current prefix to the words collection.
    Process each character in the current level in sorted order (alphabetical). For each character (except end markers):
        Extend the prefix with the current character (e.g., current_prefix + character, rather than modifying the prefix in place).
        Recursively search the child level with the extended prefix.
    Return all words found.

Complete the words_with_prefix function. This finds all words in the trie that begin with a given prefix.

    Create an empty list to store matching words.
    Keep track of the current trie level, starting at the root.
    Iterate through each character in the prefix:
        If the character doesn't exist in the current level, return an empty list: no words start with this prefix.
        If the character does exist, move to the child level corresponding to the current character.
    By now, the current level should correspond to the last character in the prefix. Use the search_level function to find all words starting from this level and return them.



from typing import Any


class Trie:
    def search_level(
    self, current_level: dict[str, Any], current_prefix: str, words: list[str]
) -> list[str]:

        if self.end_symbol in current_level:
            words.append(current_prefix)

        for char in sorted(current_level.keys()):
            if char == self.end_symbol:
                continue

            self.search_level(
                current_level[char],
                current_prefix + char,
                words
            )

        return words

    def words_with_prefix(self, prefix: str) -> list[str]:
        words = []
        current_level = self.root

        for char in prefix:
            if char not in current_level:
                return []
            current_level = current_level[char]

        return self.search_level(current_level, prefix, words)

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
