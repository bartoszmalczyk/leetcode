class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        shuffled = [""] * n
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        return "".join(shuffled)
