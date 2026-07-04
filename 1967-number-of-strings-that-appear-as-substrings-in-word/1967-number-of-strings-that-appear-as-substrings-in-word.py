class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0 
        for pattern in patterns:
            if pattern in word:
                counter += 1
        return counter