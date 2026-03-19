class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp = set()
        for c in sentence:
            temp.add(c)
        return len(temp) == 26
            