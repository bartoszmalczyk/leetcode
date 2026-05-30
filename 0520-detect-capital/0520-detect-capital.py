class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        nbr_of_capitals = 0
        for char in word:
            if char.isupper():
                nbr_of_capitals += 1
        return len(word) == nbr_of_capitals or (nbr_of_capitals == 1 and word[0].isupper()) or nbr_of_capitals == 0