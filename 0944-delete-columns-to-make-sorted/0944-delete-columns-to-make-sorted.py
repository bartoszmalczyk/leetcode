class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        n_cols = len(strs[0])
        for i in range(n_cols):
            temp = []
            for word in strs:
                temp.append(word[i])
            
            if temp != sorted(temp):
                ans += 1
                
        return ans