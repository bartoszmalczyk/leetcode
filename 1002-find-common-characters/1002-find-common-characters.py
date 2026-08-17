from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for word in words:
            common &= Counter(word)
        ans = []
        for k,v in common.items():
            for i in range(v):
                ans.append(k)
        return ans