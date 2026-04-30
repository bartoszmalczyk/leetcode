class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first_occ = -1
        for index, char in enumerate(word):
            if char == ch: 
                first_occ = index
                break
        if first_occ == -1:
            return word
        else:
            ans = ""
            for i in range(first_occ, -1, -1):
                ans += word[i]
            for j in range(first_occ + 1, len(word)):
                ans += word[j]
        return ans
                
# "abcdefd"
# "dcbaefd"